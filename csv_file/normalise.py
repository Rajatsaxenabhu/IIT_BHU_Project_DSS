import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Read the Excel file
file_path = "./Sample_Data_Site_Priority.csv"  
data = pd.read_csv(file_path)

# Display the first few rows of the original data
print("Original Data:")
print(data.head())

# Normalize the data
scaler = MinMaxScaler()
normalized_data = pd.DataFrame(scaler.fit_transform(data.select_dtypes(include=[float, int])),
                               columns=data.select_dtypes(include=[float, int]).columns)

# Combine non-numeric columns (if any) with normalized numeric data
non_numeric_data = data.select_dtypes(exclude=[float, int])
final_data = pd.concat([non_numeric_data, normalized_data], axis=1)

# Display the first few rows of the normalized data
print("Normalized Data:")
print(final_data.head())

# Save the normalized data to a new Excel file
output_path = "normalized_data.csv"
final_data.to_csv(output_path, index=False)
print(f"Normalized data saved to {output_path}")
