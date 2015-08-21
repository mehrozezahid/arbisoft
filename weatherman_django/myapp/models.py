from django.db import models

# Create your models here.


class Filename(models.Model):

    file_name = models.CharField(null=False, max_length=30, unique=True)

    def __unicode__(self):
        return self.file_name


class Filedata(models.Model):

    file_name = models.ForeignKey(Filename, related_name='fname')

    year = models.PositiveIntegerField(null=False)
    pkt = models.DateField(null=False)
    max_temperaturec = models.IntegerField(null=True, blank=True)
    mean_temperaturec = models.IntegerField(null=True, blank=True)
    min_temperaturec = models.IntegerField(null=True, blank=True)
    dew_pointc = models.IntegerField(null=True, blank=True)
    meandew_pointc = models.IntegerField(null=True, blank=True)
    mindew_pointc = models.IntegerField(null=True, blank=True)
    max_humidity = models.IntegerField(null=True, blank=True)
    mean_humidity = models.IntegerField(null=True, blank=True)
    min_humidity = models.IntegerField(null=True, blank=True)
    max_sea_level_pressurehPa = models.IntegerField(null=True, blank=True)
    mean_sea_level_pressurehPa = models.IntegerField(null=True, blank=True)
    min_sea_level_pressurehPa = models.IntegerField(null=True, blank=True)
    max_visibilityKm = models.IntegerField(null=True, blank=True)
    mean_visibilityKm = models.IntegerField(null=True, blank=True)
    min_visibilityKm = models.IntegerField(null=True, blank=True)
    max_wind_speedKmh = models.IntegerField(null=True, blank=True)
    mean_wind_speedKmh = models.IntegerField(null=True, blank=True)
    max_gust_speedkmh = models.IntegerField(null=True, blank=True)
    precipitationcm = models.FloatField(null=True, blank=True)
    cloud_cover = models.IntegerField(null=True, blank=True)
    events = models.CharField(null=True, max_length=50, blank=True)
    wind_dir_degrees = models.IntegerField(null=True, blank=True)
