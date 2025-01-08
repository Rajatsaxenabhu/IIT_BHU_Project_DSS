# from rest_framework import serializers
# from .models import DSS_DATA

# class DSS_DATASerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DSS_DATA
#         fields = '__all__'

#     def Normalize_data(self):
#         data=DSS_DATA.objects.all()
        
#         numeric_columns = ['Sewage_Gap_MLD', 'Water_quality_index', 'Mean_Temperature_Celcius', 'Mean_Rainfall_mm', 'GDDP_at_Current_Price_in_Crores', 'Number_of_Tourists', 'Number_of_ASI_Sites']

#         for field in numeric_columns:
#             values = [getattr(obj, field) for obj in data]
#             min_val,max_val= min(values),max(values)
#             for obj in data:
#                 normalised_value = (getattr(obj, field) - min_val) / (max_val - min_val) if max_val != min_val  else 0
#                 obj.normalised_value = normalised_value
#                 obj.save()

