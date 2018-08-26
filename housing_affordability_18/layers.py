from django.contrib.gis.geos import GEOSGeometry, MultiPoint, MultiPolygon, MultiLineString
from . import models

layers = {
    'housing_affordability_18_001': {
          'app_label': 'housing_affordability_18',
          'name': 'Building Permits',
          'type': 'Slide',
          'endpoint':'',
          'visualization': 'ScreenGridMap',
          'multi_geom_class': MultiPoint, 
          'model_name': models.Permit,
          'primary_attribute_column': 'new_class', # When updating primary_attribute_column, update in model as well
          'primary_attribute_label': 'New Structure Class',
          'secondary_attribute_column': 'new_type', # When updating secondary_attribute_column, update in model as well
          'secondary_attribute_label': 'New Structure Type',
          'date_attribute_column': 'issue_date',  
          'date_granularity': 'year',
          'default_date_filter': '2017',
          'min_date': '1994',
          'max_date': '2018',
        },
}

