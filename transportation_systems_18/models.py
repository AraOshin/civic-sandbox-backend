from django.contrib.gis.db import models

import django.db.models.options as options
options.DEFAULT_NAMES = options.DEFAULT_NAMES + ('in_db',)

class SafetyHotlineTickets(models.Model):
    id = models.IntegerField(primary_key=True)
    date_created = models.DateField()
    description = models.TextField(blank=True, null=True)
    geom = models.PointField(db_column = 'geom_4326')

    class Meta:
        managed = False
        app_label = 'transportation_systems_18'
        db_table = 'safety_hotline_tickets'
        in_db = 'safety_hotline_tickets'


class Sensor(models.Model):
    id = models.IntegerField(primary_key=True)
    geom_4326 = models.PointField()


    class Meta:
        managed = False
        app_label = 'transportation_systems_18'
        db_table = 'sensor_locations'
        in_db = 'pudl'






# class Crash(models.Model):
#     crash_id = models.IntegerField(primary_key=True)
#     crash_dt = models.CharField(max_length=50)
#     geom_point = models.PointField(null=True)


#     class Meta:
#         managed = False
#         db_table = 'crash'
#         in_db = 'odot_crash_data'

# class BlockChange(models.Model):
#     census_block = models.CharField(max_length=50, primary_key=True)
#     stops_pct_change = models.FloatField(max_length=50)
#     hull_4326 = models.PolygonField(null=True)


#     class Meta:
#         managed = False
#         db_table = 'census_block_change_hull'
#         in_db = 'passenger_census'

# class RouteChange(models.Model):
#     shape_id = models.CharField(max_length=50, primary_key=True)
#     pct_change = models.FloatField(max_length=50)
#     geom_linestring = models.LineStringField(null=True)


#     class Meta:
#         managed = False
#         db_table = 'route_change'
#         in_db = 'passenger_census'