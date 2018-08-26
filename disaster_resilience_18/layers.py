from django.contrib.gis.geos import GEOSGeometry, MultiPoint, MultiPolygon, MultiLineString
from . import models

layers = {
    'disaster_resilience_18_001': {
          'app_label': 'disaster_resilience_18',
          'name': 'Points of Interest',
          'type': 'Slide',
          'endpoint':'',
          'visualization': 'InconMap',
          'multi_geom_class': MultiPoint, 
          'model_name': models.POI,
          'primary_attribute_column': 'type', # When updating primary_attribute_column, update in model as well
          'primary_attribute_label': 'Type',
          'secondary_attribute_column': 'description_txt', # When updating secondary_attribute_column, update in model as well
          'secondary_attribute_label': 'Name',
          'date_attribute_column': None,
          'date_granularity': None,
          'default_date_filter': '2017',
          'min_date_override': None,
          'max_date_override': None,
        },
    'disaster_resilience_18_002': {
          'app_label': 'disaster_resilience_18',
          'name': 'Shaking',
          'type': 'Slide',
          'endpoint':'',
          'visualization': 'ChoroplethMap',
          'multi_geom_class': MultiPolygon, 
          'model_name': models.Shaking,
          'primary_attribute_column': 'pgv_site_mean_mmi_txt', # When updating primary_attribute_column, update in model as well
          'primary_attribute_label': 'Shaking Intensity Rating',
          'secondary_attribute_column': 'pgv_site_mean_desc', # When updating secondary_attribute_column, update in model as well
          'secondary_attribute_label': 'Description',
          'date_attribute_column': None,
          'date_granularity': None,
          'default_date_filter': '2018',
          'min_date_override': None,
          'max_date_override': None,
        },
    'disaster_resilience_18_003': {
          'app_label': 'disaster_resilience_18',
          'name': 'Liquefaction',
          'type': 'Slide',
          'endpoint':'',
          'visualization': 'ChoroplethMap',
          'multi_geom_class': MultiPolygon, 
          'model_name': models.Liquefaction,
          'primary_attribute_column': 'pgd_total_wet_mean_di', # When updating primary_attribute_column, update in model as well
          'primary_attribute_label': 'Total Wet Mean DI Label',
          'secondary_attribute_column': None, # When updating secondary_attribute_column, update in model as well
          'secondary_attribute_label': None,
          'date_attribute_column': None,
          'date_granularity': None,
          'default_date_filter': '2018',
          'min_date_override': None,
          'max_date_override': None,
        },
    'disaster_resilience_18_004': {
          'app_label': 'disaster_resilience_18',
          'name': 'Landslide',
          'type': 'Slide',
          'endpoint':'',
          'visualization': 'ChoroplethMap',
          'multi_geom_class': MultiPolygon, 
          'model_name': models.Landslide,
          'primary_attribute_column': 'pgd_landslide_dry_mean_di', # When updating primary_attribute_column, update in model as well
          'primary_attribute_label': 'Landslide Dry Mean DI Label',
          'secondary_attribute_column': None, # When updating secondary_attribute_column, update in model as well
          'secondary_attribute_label': None,
          'date_attribute_column': None,
          'date_granularity': None,
          'default_date_filter': '2018',
          'min_date_override': None,
          'max_date_override': None,
        },

    'disaster_resilience_18_005': {
          'app_label': 'disaster_resilience_18',
          'name': 'Points of Interest',
          'type': 'Slide',
          'endpoint':'',
          'visualization': 'ChoroplethMap',
          'multi_geom_class': MultiPolygon, 
          'model_name': models.CensusResponse,
          'primary_attribute_column': 'census_response_rate', # When updating primary_attribute_column, update in model as well
          'primary_attribute_label': 'Census Response Rate',
          'secondary_attribute_column': None, # When updating secondary_attribute_column, update in model as well
          'secondary_attribute_label': None,
          'date_attribute_column': None,
          'date_granularity': None,
          'default_date_filter': '2010',
          'min_date_override': None,
          'max_date_override': None,
        },
}