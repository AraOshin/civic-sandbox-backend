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
          'primary_attribute_column': 'description', # When updating primary_attribute_column, update in model as well
          'primary_attribute_label': 'Description',
          'secondary_attribute_column': None, # When updating secondary_attribute_column, update in model as well
          'secondary_attribute_label': None,
          'date_attribute_column': 'date_created',
          'date_granularity': 'year',
          'default_date_filter': '2017',
          'min_date': '2008',
          'max_date': '2018',
        },
    'transportation_systems_18_002': {
          'app_label': 'transportation_systems_18',
          'name': 'Sensors',
          'type': 'Slide',
          'endpoint':'',
          'visualization': 'IconMap',
          'multi_geom_class': MultiPoint, 
          'model_name': models.Sensor,
          'primary_attribute_column': None, # When updating primary_attribute_column, update in model as well
          'primary_attribute_label': None,
          'secondary_attribute_column': None, # When updating secondary_attribute_column, update in model as well
          'secondary_attribute_label': None,
          'date_attribute_column': None,
          'date_granularity': None,
          'default_date_filter': '2018',
          'min_date': None,
          'max_date': None,
        },
    'transportation_systems_18_003': {
          'app_label': 'transportation_systems_18',
          'name': 'Crashes',
          'type': 'Slide',
          'endpoint':'',
          'visualization': 'ScatterPlotMap',
          'multi_geom_class': MultiPoint, 
          'model_name': models.Crash,
          'primary_attribute_column': None, # When updating primary_attribute_column, update in model as well
          'primary_attribute_label': None,
          'secondary_attribute_column': None, # When updating secondary_attribute_column, update in model as well
          'secondary_attribute_label': None,
          'date_attribute_column': 'crash_dt',
          'date_granularity': 'year', 
          'default_date_filter': '2014',
          'min_date': '2004',
          'max_date': '2014',
        },
    'transportation_systems_18_004': {
          'app_label': 'transportation_systems_18',
          'name': 'Change in Ridership by Route',
          'type': 'Slide',
          'endpoint':'',
          'visualization': 'PathMap',
          'multi_geom_class': MultiPoint, 
          'model_name': models.RouteChange,
          'primary_attribute_column': 'pct_change', # When updating primary_attribute_column, update in model as well
          'primary_attribute_label': 'Ridership Change from 2009 to 2017', ##TODO
          'secondary_attribute_column': None, # When updating secondary_attribute_column, update in model as well
          'secondary_attribute_label': None,
          'date_attribute_column': None,
          'date_granularity': None,
          'default_date_filter': '2017',
          'min_date': None,
          'max_date': None,
        },
    'transportation_systems_18_005': {
          'app_label': 'transportation_systems_18',
          'name': 'Change in Ridership by Census Block',
          'type': 'Slide',
          'endpoint':'',
          'visualization': 'ChoroplethMap',
          'multi_geom_class': MultiPoint, 
          'model_name': models.BlockChange,
          'primary_attribute_column': 'stops_pct_change', # When updating primary_attribute_column, update in model as well
          'primary_attribute_label': 'Ridership Change from 2009 to 2017',
          'secondary_attribute_column': None, # When updating secondary_attribute_column, update in model as well
          'secondary_attribute_label': None,
          'date_attribute_column': None,
          'date_granularity': None,
          'default_date_filter': '2017',
          'min_date': None,
          'max_date': None,
        },
}
