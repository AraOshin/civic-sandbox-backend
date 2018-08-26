from django.contrib.gis.geos import GEOSGeometry, MultiPoint, MultiPolygon, MultiLineString
from . import models

layers = {
    'housing_affordability_18_001': {
          'app_label': 'housing_affordability_18',
          'name': 'Building Permits',
          'type': 'Slide',
          'endpoint':'',
          'visualization': 'ScatterPlotMap',
          'multi_geom_class': MultiPoint, 
          'model_name': models.Permit,
          'date_attribute_column': None, ##TODO 
          'date_granularity': None,
          'default_date_filter': None,
          'min_date_override': None,
          'max_date_override': None,
        },
}


# permits_meta = {
#   'attributes': {
#     'primary': {
#       'field': 'new_class',
#       'name': 'New Structure Class',
#     },
#     'secondary': {
#       'field': 'new_type',
#       'name': 'New Structure Type',
#     },
#   },
#   'dates': {
#   'date_attribute': 'issue_date',
#   'date_granularity': 'year',
#   'default_date_filter': '2017',
#   'min_date': '1994',
#   'max_date': '2018',
#     },
#   }
