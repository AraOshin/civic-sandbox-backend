from django.contrib.gis.geos import GEOSGeometry, MultiPoint, MultiPolygon, MultiLineString
from . import models

layers = {
    'transportation_systems_18_001': {
          'app_label': 'transportation_systems_18',
          'name': 'Safety Hotline',
          'type': 'Slide',
          'endpoint':'',
          'visualization': 'ScatterPlotMap',
          'multi_geom_class': MultiPoint, 
          'model_name': models.SafetyHotlineTickets,
          'date_attribute_column': None,
          'date_granularity': 'year',
          'default_date_filter': None,
          'min_date_override': 'todo',
          'max_date_override': 'todo',
        },
    'transportation_systems_18_002': {
          'app_label': 'transportation_systems_18',
          'name': 'Sensors',
          'type': 'Slide',
          'endpoint':'',
          'visualization': 'IconMap',
          'multi_geom_class': MultiPoint, 
          'model_name': models.Sensor,
          'date_attribute_column': None,
          'date_granularity': None,
          'default_date_filter': None,
          'min_date_override': None,
          'max_date_override': None,
        },
}




#     'layers': {
#         '015': {
#           'name': 'Change in Ridership by Route',
#           'endpoint':'http://service.civicpdx.org/transportation-systems/sandbox/slides/routechange/',
#           'visualization': 'PathMap',

#         },
#         '032': {
#           'name': 'Crashes',
#           'endpoint':'http://service.civicpdx.org/transportation-systems/sandbox/slides/crashes/',
#           'visualization': 'ScatterPlotMap',
#         },
#         '042': {
#           'name': 'Change in Ridership by Census Block',
#           'endpoint':'http://service.civicpdx.org/transportation-systems/sandbox/foundations/blockchange/',
#           'visualization': 'ChoroplethMap',
#         },
# }
