from django.contrib.gis.geos import GEOSGeometry, MultiPoint, MultiPolygon, MultiLineString

layers = {
        # '003': { #TODO deal with unique keys in dicts in seperate files ##TODO add category groupings? 
        #     'app_label': '',
        #     'name': 'Change in Ridership by Route',
        #     'type': 'Slide',
        #     'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/foundations/reportsbymonth/',
        #     'visualization': 'ChoroplethMap',
        #     'db_table_name': 'bike_parking',
        #     'id_column': 'objectid',
        #     'id_column_type': 'IntegerField',
        #     'geom_column': 'geom',
        #     'geom_column_type': 'PointField',
        #     'multi_geom_class': MultiPoint, 
        #     'primary_attribute_column': None,
        #     'primary_attribute_column_type': None,
        #     'secondary_attribute_column': None, 
        #     'secondary_attribute_column_type': None,
        #     'model_name': 'BikeParkingModel',
        #     'date_attribute': None,
        #     'date_column_type': None,
        #     'date_granularity': None,
        #     'default_date_filter': '2017',
        #     'min_date_override': None, #TODO
        #     'max_date_override': None, #TODO
        #   },
    'transportation_systems_18_001': {
          'app_label': 'transportation_systems_18',
          'name': 'Safety Hotline',
          'type': 'Slide',
          'endpoint':'',
          'visualization': 'ScatterPlotMap',
          'multi_geom_class': MultiPoint, 
        #   'model_name': models.CampReport,
          'date_attribute_column': 'date_created',
          'date_granularity': 'year',
          'default_date_filter': '2017',
          'min_date_override': 'todo',
          'max_date_override': 'todo',
        },
}




#     'layers': {
#         '015': {
#           'name': 'Change in Ridership by Route',
#           'endpoint':'http://service.civicpdx.org/transportation-systems/sandbox/slides/routechange/',
#           'visualization': 'PathMap',
#         },
#         '016': {
#           'name': 'points of interest',
#           'endpoint':'http://service.civicpdx.org/disaster-resilience/sandbox/slides/poi/',
#           'visualization': 'IconMap',
#         },
#         '031': {
#           'name': 'Safety Hotline',
#           'endpoint':'http://service.civicpdx.org/transportation-systems/sandbox/slides/safetyhotline/',
#           'visualization': 'ScatterPlotMap',
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
