from django.contrib.gis.db import models


class Permit(models.Model):
    id = models.IntegerField(primary_key=True)
    issue_date = models.DateTimeField()
    new_class = models.CharField(max_length=255)
    new_type = models.CharField(max_length=255)
    geom = models.PointField(db_column='point')

    class Meta:
        managed = False
        db_table = 'api_permitdata'