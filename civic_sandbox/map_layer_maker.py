
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
        self.model_name = layers[layer_key]['model_name']
        self.multi_geom_class = layers[layer_key]['multi_geom_class']
        self.date_attribute_column = layers[layer_key]['date_attribute_column'] 
        self.default_date_filter = layers[layer_key]['default_date_filter']
    
    def get_serializer(self):
    
        class SandboxSerializer(GeoFeatureModelSerializer):
            class Meta:
                model = self.model_name
                fields = '__all__'
                geo_field = 'geom'

        return SandboxSerializer
    
    def get_view(self):
        
        serializer_class=self.get_serializer()

        @api_view(['GET'])
        def sandbox_function(request, date_filter=self.default_date_filter, format=None): 

            ## get data ##
            try:
                if not self.date_attribute_column: 
                    dataset = self.model_name.objects.all()
                else:
                    variable_column = self.date_attribute_column
                    filter = variable_column + '__contains'
                    dataset = self.model_name.objects.filter(**{ filter: date_filter })
                    if settings.DEBUG: print('---------------------------------------')
                    if settings.DEBUG: print(filter)
                    if settings.DEBUG: print(date_filter)

                if settings.DEBUG: print('made queryset')

            # calculate limit boundary meta #
                coords = []
                for each in dataset: 
     
                    geom = getattr(each, 'geom')
     
                    if geom is not None: 
                    ## converts MultiPolygons to Polygons ##
                        if isinstance(geom, MultiPolygon):
                            coords.append(geom.convex_hull)
                        else: 
                            coords.append(geom) 
                multi = self.multi_geom_class(coords)

                limit_boundary = multi.convex_hull.json

                if settings.DEBUG: print('boundary calculation complete')
                
            except self.model_name.DoesNotExist:
                return Response(status.HTTP_404_NOT_FOUND)

            if settings.DEBUG: print(serializer_class)
            serializer = serializer_class(dataset, many=True)


            response= { 
                'meta': {
                    'boundary': [json.loads(limit_boundary)],
                    },
                'data': serializer.data
            }

            return Response(response)

        return sandbox_function

