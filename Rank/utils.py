import csv
from django.conf import settings
from .models import DistrictData
from django.shortcuts import render

def load_csv_data():
    file_path = settings.BASE_DIR / 'csv_file/normalized_data.csv' 
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Use update_or_create to avoid duplicates and update existing records
            DistrictData.objects.update_or_create(
                district=row['Districts'],  # Use 'Districts' column as the lookup key
                defaults={
                    'sewage_gap_mld': row['Sewage_Gap_MLD'],
                    'water_quality_index': row['Water_quality_index'],
                    'mean_temperature_celsius': row['Mean_Temperature_Celcius'],
                    'mean_rainfall_mm': row['Mean_Rainfall_mm'],
                    'gddp_at_current_price_in_crore': row['GDDP_at_Current_Price_in_Crore'],
                    'number_of_tourists': row['Number_of_Tourists'],
                    'number_of_asi_sites': row['Number_of_ASI_Sites']
                }
            )
    return "Data loaded successfully"