from django.db import models

class DistrictData(models.Model):
    id = models.AutoField(primary_key=True)
    district = models.CharField(max_length=100)
    sewage_gap_mld = models.FloatField()
    water_quality_index = models.FloatField()
    mean_temperature_celsius = models.FloatField()
    mean_rainfall_mm = models.FloatField()
    gddp_at_current_price_in_crore = models.FloatField()
    number_of_tourists = models.FloatField()
    number_of_asi_sites = models.FloatField()

    def __str__(self):
        return self.district

