
from django.contrib.gis.db import models
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework.serializers import ModelSerializer
from django.contrib.gis.geos import GEOSGeometry, MultiPoint, MultiPolygon, MultiLineString
import json 
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
from .all_layers import layers


class SandboxMaker: 
    def __init__(self, layer_key):
        self.app_label = layers[layer_key]['app_label']
        self.db_table_name = layers[layer_key]['db_table_name']
        self.id_column = layers[layer_key]['id_column']
        self.id_column_type = layers[layer_key]['id_column_type']
        self.geom_column = layers[layer_key]['geom_column']
        self.geom_column_type = layers[layer_key]['geom_column_type']
        self.multi_geom_class = layers[layer_key]['multi_geom_class']
        self.primary_attribute_column = layers[layer_key]['primary_attribute_column']
        self.primary_attribute_column_type = layers[layer_key]['primary_attribute_column_type']
        self.secondary_attribute_column = layers[layer_key]['secondary_attribute_column']
        self.secondary_attribute_column_type = layers[layer_key]['secondary_attribute_column_type']
        self.date_attribute = layers[layer_key]['date_attribute'] ##todo rename column? for consistancy? 
        self.date_column_type = layers[layer_key]['date_column_type']
        self.default_date_filter = layers[layer_key]['default_date_filter']
        self.model_name = layers[layer_key]['model_name']
        self.model_class = self.get_model()
        

        

    def get_model(self):

        class Meta:
            managed = False
            db_table = self.db_table_name
            app_label = self.app_label

        attrs = {
            self.id_column: getattr(models, self.id_column_type)(primary_key=True),
            'geom': getattr(models, self.geom_column_type)(db_column=self.geom_column),
            '__module__': 'civic_sandbox.models', 
            'Meta': Meta
        }

        if self.primary_attribute_column is not None: 
            attrs[self.primary_attribute_column] = getattr(models, self.primary_attribute_column_type)(max_length=300) ##TODO max_length dynamic or use TextField? 
                
        if self.secondary_attribute_column is not None: 
            attrs[self.secondary_attribute_column] = getattr(models, self.secondary_attribute_column_type)(max_length=300)
        
        if self.date_attribute is not None: 
            attrs[self.date_attribute] = getattr(models, self.date_column_type)(max_length=50) ##TODO max_length dynamic or use TextField? 
                

        SandboxModel = type(self.model_name, (models.Model,), attrs)

        return SandboxModel
    
    def get_serializer(self):
    
        class SandboxSerializer(GeoFeatureModelSerializer):
            class Meta:
                model = self.model_class
                fields = '__all__'
                geo_field = 'geom'

        return SandboxSerializer
    
    def get_view(self):
        
        serializer_class=self.get_serializer()

        @api_view(['GET'])
        def sandbox_function(request, date_filter=self.default_date_filter, format=None): 

            ## get data ##
            try:
                if not self.date_attribute: 
                    dataset = self.model_class.objects.all()
                else:
                    variable_column = self.date_attribute
                    filter = variable_column + '__contains'
                    dataset = self.model_class.objects.filter(**{ filter: date_filter })
                    if settings.DEBUG: print('---------------------------------------')
                    if settings.DEBUG: print(filter)
                    if settings.DEBUG: print(date_filter)

                if settings.DEBUG: print('made queryset')

            # calculate limit boundary meta #
                coords = []
                for each in dataset: 
                    # my_geom = each.geom
     
                    geom = getattr(each, self.geom_column)
     
                    if geom is not None: 
                    ## converts MultiPolygons to Polygons ##
                        if isinstance(geom, MultiPolygon):
                            coords.append(geom.convex_hull)
                        else: 
                            coords.append(geom) 
                multi = self.multi_geom_class(coords)

                limit_boundary = multi.convex_hull.json

                if settings.DEBUG: print('boundary calculation complete')
                
            except self.model_class.DoesNotExist:
                return Response(status.HTTP_404_NOT_FOUND)

            if settings.DEBUG: print(serializer_class)
            serializer = serializer_class(dataset, many=True)



            response= { 
                'meta': {
                    'boundary': [json.loads(limit_boundary)],
                    ##TODO add calculated min and max date 
                    },
                'data': serializer.data
            }

            return Response(response)

        return sandbox_function

