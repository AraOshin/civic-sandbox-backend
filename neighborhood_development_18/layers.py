from django.contrib.gis.geos import GEOSGeometry, MultiPoint, MultiPolygon, MultiLineString

layers = {
        '001': { #TODO deal with unique keys in dicts in seperate files ##TODO add category groupings? 
            'app_label': 'neighborhood_development_18',
            'name': 'Bike Parking',
            'type': 'Slide',
            'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/foundations/reportsbymonth/',
            'visualization': 'ChoroplethMap',
            'db_table_name': 'bike_parking',
            'id_column': 'objectid',
            'id_column_type': 'IntegerField',
            'geom_column': 'geom',
            'geom_column_type': 'PointField',
            'multi_geom_class': MultiPoint, 
            'primary_attribute_column': None,
            'primary_attribute_column_type': None,
            'secondary_attribute_column': None, 
            'secondary_attribute_column_type': None,
            'model_name': 'BikeParkingModel',
            'date_attribute': None,
            'date_column_type': None,
            'date_granularity': None,
            'default_date_filter': '2017',
            'min_date_override': None, #TODO
            'max_date_override': None, #TODO
          },
        '011': {
          'app_label': 'neighborhood_development_18',
          'name': 'demolitions',
          'type': 'Slide',
          'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/slides/demolitions/',
          'visualization': 'ScatterPlotMap',
          'db_table_name': 'demolitions',
          'id_column': 'objectid',
          'id_column_type': 'IntegerField',
          'geom_column': 'geom',
          'geom_column_type': 'PointField',
          'multi_geom_class': MultiPoint, 
          'primary_attribute_column': 'description',
          'primary_attribute_column_type': 'CharField',
          'secondary_attribute_column': None, 
          'secondary_attribute_column_type': None,
          'model_name': 'DemolitionsModel',
          'date_attribute': 'year', ##rename as column 
          'date_column_type': 'CharField',
          'date_granularity': 'year',
          'default_date_filter': '2018',
          'min_date': '2000',
          'max_date': '2018',
  },
}


