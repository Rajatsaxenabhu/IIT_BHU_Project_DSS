# Generated by Django 5.1.4 on 2025-01-12 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DistrictData",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("district", models.CharField(max_length=100)),
                ("sewage_gap_mld", models.FloatField()),
                ("water_quality_index", models.FloatField()),
                ("mean_temperature_celsius", models.FloatField()),
                ("mean_rainfall_mm", models.FloatField()),
                ("gddp_at_current_price_in_crore", models.FloatField()),
                ("number_of_tourists", models.FloatField()),
                ("number_of_asi_sites", models.FloatField()),
                ("app_Rank", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Weight",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("temp", models.CharField(default="temp")),
                ("Sewage_Gap_MLD", models.FloatField(default=0.34)),
                ("Water_quality_index", models.FloatField(default=0.24)),
                ("Mean_Temperature_Celcius", models.FloatField(default=0.15)),
                ("Mean_Rainfall_mm", models.FloatField(default=0.09)),
                ("GDDP_at_Current_Price_in_Crore", models.FloatField(default=0.08)),
                ("Number_of_Tourists", models.FloatField(default=0.06)),
                ("Number_of_ASI_Sites", models.FloatField(default=0.04)),
            ],
        ),
    ]