from django.contrib.gis.geos import GEOSGeometry, MultiPoint, MultiPolygon, MultiLineString
from . import models

layers = {
        'neighborhood_development_18_001': { 
            'app_label': 'neighborhood_development_18',
            'name': 'Bike Parking',
            'type': 'Slide',
            'endpoint':'',
            'visualization': 'ScatterPlotMap',
            'multi_geom_class': MultiPoint, 
            'model_name': models.BikeParking,
            'primary_attribute_column': None, # When updating primary_attribute_column, update in model as well
            'primary_attribute_label': None,
            'secondary_attribute_column': None, # When updating secondary_attribute_column, update in model as well
            'secondary_attribute_label': None,
            'date_attribute_column': None, 
            'date_granularity': None,
            'default_date_filter': '2017',
            'min_date': None,
            'max_date': None, 
        },
        'neighborhood_development_18_002': {
          'app_label': 'neighborhood_development_18',
          'name': 'Bike Lanes',
          'type': 'Slide',
          'endpoint':'',
          'visualization': 'PathMap',
          'primary_attribute_column': None, # When updating primary_attribute_column, update in model as well
          'primary_attribute_label': None,
          'secondary_attribute_column': None, # When updating secondary_attribute_column, update in model as well
          'secondary_attribute_label': None,
          'multi_geom_class': MultiLineString, 
          'model_name': models.BikeLane,
          'date_attribute_column': None, 
          'date_granularity': None,
          'default_date_filter': '2018',
          'min_date': None,
          'max_date': None,
        },
        'neighborhood_development_18_003': {
          'name': 'Parks',
          'type': 'Slide',
          'endpoint':'',
          'visualization': 'PolygonPlotMap', 
          'multi_geom_class': MultiPolygon, 
          'model_name': models.Park,
          'primary_attribute_column': 'name', # When updating primary_attribute_column, update in model as well
          'primary_attribute_label': 'Park',
          'secondary_attribute_column': 'acres', # When updating secondary_attribute_column, update in model as well
          'secondary_attribute_label': 'Park Acreage',
          'date_attribute_column': None, 
          'date_granularity': None,
          'default_date_filter': '2018',
          'min_date': None,
          'max_date': None,
        },
        'neighborhood_development_18_004': {
          'name': 'Multi-use Trails',
          'type': 'Slide',
          'endpoint':'',
          'visualization': 'PathMap',
          'multi_geom_class': MultiLineString, 
          'model_name': models.MultiuseTrail,
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
        'neighborhood_development_18_005': {
          'name': 'Community Gardens',
          'type': 'Slide',
          'endpoint':'',
          'visualization': 'SmallPolygonMap',
          'multi_geom_class': MultiPolygon, 
          'model_name': models.CommunityGarden,
          'primary_attribute_column': 'sitename', # When updating primary_attribute_column, update in model as well
          'primary_attribute_label': 'Name',
          'secondary_attribute_column': None, # When updating secondary_attribute_column, update in model as well
          'secondary_attribute_label': None,
          'date_attribute_column': None, 
          'date_granularity': None,
          'default_date_filter': '2017',
          'min_date': None,
          'max_date': None,
        },
        'neighborhood_development_18_006': {
          'name': 'Bike Greenways',
          'type': 'Slide',
          'endpoint':'',
          'visualization': 'PathMap',
          'multi_geom_class': MultiLineString, 
          'model_name': models.BikeGreenway,
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
        'neighborhood_development_18_007': {
          'name': 'Rail Stops',
          'type': 'Slide',
          'endpoint':'',
          'visualization': 'ScatterPlotMap',
          'multi_geom_class': MultiPoint, 
          'model_name': models.RailStop,
          'primary_attribute_column': None, # When updating primary_attribute_column, update in model as well
          'primary_attribute_label': None,
          'secondary_attribute_column': None, # When updating secondary_attribute_column, update in model as well
          'secondary_attribute_label': None,
          'date_attribute_column': None, 
          'date_granularity': None,
          'default_date_filter': '2016',
          'min_date': None,
          'max_date': None,
        },
        'neighborhood_development_18_008': {
          'name': 'Grocery Stores',
          'type': 'Slide',
          'endpoint':'',
          'visualization': 'ScatterPlotMap',
          'multi_geom_class': MultiPoint, 
          'model_name': models.RailStop,
          'primary_attribute_column': 'company_na', # When updating primary_attribute_column, update in model as well
          'primary_attribute_label': 'Name',
          'secondary_attribute_column': None, # When updating secondary_attribute_column, update in model as well
          'secondary_attribute_label': None,
          'date_attribute_column': None, 
          'date_granularity': None,
          'default_date_filter': '2018',
          'min_date': None,
          'max_date': None,
        },
        'neighborhood_development_18_009': {
          'name': 'Demolitions',
          'type': 'Slide',
          'endpoint':'',
          'visualization': 'ScatterPlotMap',
          'multi_geom_class': MultiPoint, 
          'model_name': models.Demolition,
          'primary_attribute_column': None, # When updating primary_attribute_column, update in model as well
          'primary_attribute_label': None,
          'secondary_attribute_column': None, # When updating secondary_attribute_column, update in model as well
          'secondary_attribute_label': None,
          'date_attribute_column': 'year', 
          'date_granularity': 'year',
          'default_date_filter': '2018',
          'min_date': '2000',
          'max_date': '2018',
        },
        'neighborhood_development_18_010': {
          'app_label': 'neighborhood_development_18',
          'name': 'Camp Sweeps',
          'type': 'Slide',
          'endpoint':'',
          'visualization': 'ScatterPlotMap',
          'multi_geom_class': MultiPoint, 
          'model_name': models.CampSweep,
          'primary_attribute_column': None, # When updating primary_attribute_column, update in model as well
          'primary_attribute_label': None,
          'secondary_attribute_column': None, # When updating secondary_attribute_column, update in model as well
          'secondary_attribute_label': None,
          'date_attribute_column': 'formatted_date',
          'date_granularity': 'month',
          'default_date_filter': 'Apr2018',
          'min_date': 'Oct2016',
          'max_date': 'May2018',
        },
        'neighborhood_development_18_011': {
          'app_label': 'neighborhood_development_18',
          'name': 'Camp Reports',
          'type': 'Slide',
          'endpoint':'',
          'visualization': 'ScatterPlotMap',
          'multi_geom_class': MultiPoint, 
          'model_name': models.CampReport,
          'primary_attribute_column': None, # When updating primary_attribute_column, update in model as well
          'primary_attribute_label': None,
          'secondary_attribute_column': None, # When updating secondary_attribute_column, update in model as well
          'secondary_attribute_label': None,
          'date_attribute_column': 'date',
          'date_granularity': 'year',
          'default_date_filter': '2018',
          'min_date': '2015',
          'max_date': '2018',
        },
        'neighborhood_development_18_012': {
          'app_label': 'neighborhood_development_18',
          'name': 'Bus Stops',
          'type': 'Slide',
          'endpoint':'',
          'visualization': 'ScatterPlotMap',
          'multi_geom_class': MultiPoint, 
          'model_name': models.BusStop,
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
        'neighborhood_development_18_045': {
          'app_label': 'neighborhood_development_18',
          'name': 'Monthly Campsite Reports',
          'type': 'Foundation',
          'endpoint':'',
          'visualization': 'ChoroplethMap',
          'multi_geom_class': MultiPolygon, 
          'model_name': models.ReportsByMonth,
          'primary_attribute_column': 'count', # When updating primary_attribute_column, update in model as well
          'primary_attribute_label': 'Count',
          'secondary_attribute_column': None, # When updating secondary_attribute_column, update in model as well
          'secondary_attribute_label': None,
          'date_attribute_column': 'formatted_date',
          'date_granularity': 'month',
          'default_date_filter': 'Apr2018', 
          'min_date': 'Dec2015',
          'max_date': 'Apr2018',
        },
        'neighborhood_development_18_013': {
          'app_label': 'neighborhood_development_18',
          'name': 'Bike Estimates',
          'type': 'Slide',
          'endpoint':'',
          'visualization': 'ScatterPlotMap',
          'multi_geom_class': MultiPoint, 
          'model_name': models.BikeDailyEstimate,
          'primary_attribute_column': 'year_2016', # When updating primary_attribute_column, update in model as well
          'primary_attribute_label': 'Daily Estimates of Bike Traffic',
          'secondary_attribute_column': None, # When updating secondary_attribute_column, update in model as well
          'secondary_attribute_label': None,
          'date_attribute_column': None,
          'date_granularity': None,
          'default_date_filter': '2016',
          'min_date': None,
          'max_date': None,
        },
        'neighborhood_development_18_014': {
          'app_label': 'neighborhood_development_18',
          'name': 'Bike Counts',
          'type': 'Slide',
          'endpoint':'',
          'visualization': 'ScatterPlotMap',
          'multi_geom_class': MultiPolygon, 
          'model_name': models.BikeCount,
          'primary_attribute_column': 'year_2017', # When updating primary_attribute_column, update in model as well
          'primary_attribute_label': 'Actual Bike Count',
          'secondary_attribute_column': 'count_time', # When updating secondary_attribute_column, update in model as well
          'secondary_attribute_label': 'Count Time',
          'date_attribute_column': None, 
          'date_granularity': None,
          'default_date_filter': '2017',
          'min_date': None,
          'max_date': None,
        },
}




      
        # '007': {
        #   'name': 'Total Population',
        #   'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/foundations/population/',
        #   'visualization': 'ChoroplethMap',
        # },
        # '018': {
        #   'name': 'Median Houshold Income',
        #   'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/foundations/income/',
        #   'visualization': 'ChoroplethMap',
        # },
        # '019': {
        #   'name': 'Median Gross Rent',
        #   'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/foundations/grossrent/',
        #   'visualization': 'ChoroplethMap',
        # },
        # '020': {
        #   'name': 'Evictions',
        #   'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/foundations/evictions/',
        #   'visualization': 'ChoroplethMap',
        # },
        # '021': {
        #   'name': 'Renter Occupied Households',
        #   'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/foundations/renteroccupied/',
        #   'visualization': 'ChoroplethMap',
        # },
        # '022': {
        #   'name': 'Rent Burden',
        #   'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/foundations/rentburden/',
        #   'visualization': 'ChoroplethMap',
        # },
        # '024': {
        #   'name': 'Households with Children',
        #   'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/foundations/under18/',
        #   'visualization': 'ChoroplethMap',
        # },
        # '025': {
        #   'name': 'Households with Seniors',
        #   'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/foundations/over65/',
        #   'visualization': 'ChoroplethMap',
        # },
        # '026': {
        #   'name': 'Housholders Living Alone',
        #   'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/foundations/livingalone/',
        #   'visualization': 'ChoroplethMap',
        # },
        # '027': {
        #   'name': 'Owner Occupied Housholds',
        #   'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/foundations/owneroccupied/',
        #   'visualization': 'ChoroplethMap',
        #  },
        # '028': {
        #   'name': 'Percent Renter Occupied',
        #   'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/foundations/pctrenteroccupied/',
        #   'visualization': 'ChoroplethMap',
        # },
        # '037': {
        #   'name': 'Voters 18 to 25',
        #   'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/foundations/voters18to25/',
        #   'visualization': 'ChoroplethMap',
        # },
        # '038': {
        #   'name': 'Voters 26 to 32',
        #   'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/foundations/voters26to32/',
        #   'visualization': 'ChoroplethMap',
        # },
        # '039': {
        #   'name': 'Voters 33 to 39',
        #   'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/foundations/voters33to39/',
        #   'visualization': 'ChoroplethMap',
        # },
        # '040': {
        #   'name': 'Voters 40 to 49',
        #   'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/foundations/voters40to49/',
        #   'visualization': 'ChoroplethMap',
        # },
        # '041': {
        #   'name': 'Voters 50 plus',
        #   'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/foundations/voters50plus/',
        #   'visualization': 'ChoroplethMap',
        # },
        # '042': {
        #   'name': 'Change in Ridership by Census Block',
        #   'endpoint':'http://service.civicpdx.org/transportation-systems/sandbox/foundations/blockchange/',
        #   'visualization': 'ChoroplethMap',
        # },
        # '043': {
        #   'name': 'Eviction Rate',
        #   'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/foundations/evictionrate/',
        #   'visualization': 'ChoroplethMap',
        # },
        # '044': {
        #   'name': 'Poverty Rate',
        #   'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/foundations/povertyrate/',
        #   'visualization': 'ChoroplethMap',
        # },
