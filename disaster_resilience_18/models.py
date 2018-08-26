from django.contrib.gis.db import models

class POI(models.Model): 
    pk_id= models.CharField(primary_key=True, max_length=30,)
    type = models.CharField(max_length=20)
    description2_txt = models.CharField(max_length=60)
    geom = models.PointField(db_column = 'wkb_geometry')

    class Meta:
        managed = False
        db_table = 'POI_view'

class Shaking(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80)
    geom = models.GeometryField(db_column='wkb_geometry')
    pgv_site_mean_mmi_txt = models.CharField(max_length=10)
    pgv_site_mean_desc = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'disaster_neighborhood_view'



class Liquefaction(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80)
    geom = models.GeometryField(db_column='wkb_geometry')
    pgd_total_wet_mean_di = models.CharField(max_length=50) 


    class Meta:
        managed = False
        db_table = 'disaster_neighborhood_view'


class Landslide(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80)
    geom = models.GeometryField(db_column='wkb_geometry')
    pgd_landslide_dry_mean_di = models.CharField(max_length=50)


    class Meta:
        managed = False
        db_table = 'disaster_neighborhood_view'

class CensusResponse(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80)
    geom = models.GeometryField(db_column='wkb_geometry')
    census_response_rate = models.FloatField()

    class Meta:
        managed = False
        db_table = 'disaster_neighborhood_view'