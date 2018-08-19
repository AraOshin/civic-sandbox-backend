##TODO: write comments: 
## geometry column must be named geom, instructions for renaming 
## updates to the field name for primary or secondary attribute fields must al;so be changed in layers.py 

from django.contrib.gis.db import models

##TODO: add layer key comments: 


class BikeParking(models.Model):
    objectid = models.IntegerField(primary_key=True)
    geom = models.PointField()

    class Meta:
        managed = False
        db_table = 'bike_parking'
        app_label = 'neighborhood_development_18'


class Demolition(models.Model):
    objectid = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=4000)
    year = models.CharField(max_length=50)
    geom = models.PointField()

    class Meta:
        managed = False
        db_table = 'demolitions'
        app_label = 'neighborhood_development_18'   

class BikeLane(models.Model):
    objectid = models.IntegerField(primary_key=True)
    geom = models.LineStringField()

    class Meta:
        managed = False
        db_table = 'bike_lanes'
        app_label = 'neighborhood_development_18'

class Park(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    acres = models.FloatField()
    geom = models.GeometryField()

    class Meta:
        managed = False
        db_table = 'parks'
        app_label = 'neighborhood_development_18'

class MultiuseTrail(models.Model):
    ogc_fid = models.IntegerField(primary_key=True)
    geom = models.LineStringField()

    class Meta:
        managed = False
        db_table = 'active_multiuse_trail'
        app_label = 'neighborhood_development_18'

class CommunityGarden(models.Model):
    id = models.IntegerField(primary_key=True)
    sitename = models.CharField(max_length=50)
    geom = models.GeometryField()

    class Meta:
        managed = False
        db_table = 'community_gardens'
        app_label = 'neighborhood_development_18'

class BikeGreenway(models.Model):
    objectid = models.IntegerField(primary_key=True)
    geom = models.GeometryField()

    class Meta:
        managed = False
        db_table = 'bike_greenways'
        app_label = 'neighborhood_development_18'

class RailStop(models.Model):
    id = models.IntegerField(primary_key=True)
    geom = models.PointField()

    class Meta:
        managed = False
        db_table = 'rail_stops'
        app_label = 'neighborhood_development_18'


class CampSweep(models.Model):
    id = models.IntegerField(primary_key=True)
    formatted_date = models.CharField(max_length=50)
    geom = models.PointField()

    class Meta:
        managed = False
        db_table = 'camp_sweeps_view'
        app_label = 'neighborhood_development_18'


class CampReport(models.Model):
    id = models.IntegerField(db_column='ItemID', primary_key=True)
    date = models.DateTimeField()
    geom = models.PointField()

    class Meta:
        managed = False
        db_table = 'campsite_reports'
        app_label = 'neighborhood_development_18'

class RetailGrocer(models.Model):
    id = models.IntegerField(primary_key=True)
    company_na = models.CharField('name', help_text='primary_attribute', max_length=50)
    geom = models.GeometryField()

    class Meta:
        managed = False
        db_table = 'retail_grocers'
        app_label = 'neighborhood_development_18'

# class BusStop(models.Model):

#     keyitem = models.CharField(primary_key=True, max_length=50)
#     geom = models.PointField()

#     class Meta:
#         managed = False
#         db_table = 'bus_stops'

# # class IMSNeighborhood(models.Model):
# #     id = models.IntegerField(primary_key=True)
# #     year = models.CharField(max_length=50)
# #     total_population = models.IntegerField()
# #     pc_household_with_children_under_18 = models.FloatField()
# #     pc_household_with_individuals_65_ovr = models.FloatField()
# #     pc_owner_occupied_housing_units = models.FloatField()
# #     pc_householders_living_alone = models.FloatField()
# #     geom = models.GeometryField()

# #     class Meta:
# #         managed = False
# #         db_table = 'ims_neighborhood_demographics'

# # class BlockGroup(models.Model):
# #     id = models.IntegerField(primary_key=True)
# #     year = models.CharField(max_length=50)
# #     median_household_income = models.IntegerField()
# #     Median_gross_rent = models.IntegerField()
# #     evictions = models.IntegerField()
# #     eviction_rate = models.FloatField() 
# #     renter_occupied_households = models.IntegerField()
# #     rent_burden = models.FloatField()
# #     poverty_rate = models.FloatField() 
# #     pctrenter_occupied = models.FloatField()
# #     geom = models.PolygonField()
# #     class Meta:
# #         managed = False
# #         db_table = 'evictions_blockgroups_scope'


# # class NeighborhoodVoterRegistrationByAgeGroup(models.Model):
# #     neighborhood = models.TextField()
# #     id = models.IntegerField(primary_key=True)
# #     year = models.IntegerField()
# #     pct_18_25 = models.FloatField()
# #     pct_26_32 = models.FloatField()
# #     pct_33_39 = models.FloatField()
# #     pct_40_49 = models.FloatField()
# #     pct_50_plus = models.FloatField()
# #     geom = models.GeometryField()
    

#     # class Meta:
#     #     managed = False
#     #     db_table = 'neighborhood_voters_ages_over_time_geom'

class ReportsByMonth(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80)
    formatted_date = models.CharField(max_length=50)
    count = models.IntegerField()
    geom = models.GeometryField()

    class Meta:
        managed = False
        db_table = 'campsite_reports_by_month_neigh'
        app_label = 'neighborhood_development_18'


# class BikeCount(models.Model):
#    id = models.IntegerField(primary_key=True)
#    count_time = models.CharField(max_length=5)
#    year_2017 = models.IntegerField(db_column="2017", blank=True, null=True)
#    geom = models.PointField(blank=True, null=True)

#    class Meta:
#        managed = False
#        db_table = "bike_counts"


# class BikeDailyEstimate(models.Model):
#    id = models.IntegerField(primary_key=True)
#    year_2016 = models.IntegerField(db_column="2016", blank=True, null=True)
#    geom = models.PointField(blank=True, null=True)


#    class Meta:
#        managed = False
#        db_table = "bike_daily_estimates"