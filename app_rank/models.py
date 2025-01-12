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
    app_Rank=models.IntegerField(default=0)


    def __str__(self):
        return self.district
    
class Weight(models.Model):
    temp=models.CharField(default='temp')
    Sewage_Gap_MLD=models.FloatField(default=0.34,null=False)
    Water_quality_index=models.FloatField(default=0.24,null=False)
    Mean_Temperature_Celcius=models.FloatField(default=0.15,null=False)
    Mean_Rainfall_mm=models.FloatField(default=0.09,null=False)
    GDDP_at_Current_Price_in_Crore=models.FloatField(default=0.08,null=False)
    Number_of_Tourists=models.FloatField(default=0.06,null=False)
    Number_of_ASI_Sites=models.FloatField(default=0.04,null=False)

    
    def check_weights(self):
        total = sum([getattr(self, field) for field in self._meta.get_fields() if isinstance(getattr(self, field), float)])
        if total!=1:
            return False
        return True

