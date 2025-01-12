import pandas as pd
import psycopg2
from psycopg2 import sql

# Define the PostgreSQL connection parameters
host = "localhost"  # Replace with your host
port = "5432"  # Replace with your port
dbname = "mydatabase"  # Replace with your database name
user = "myuser"  # Replace with your PostgreSQL username
password = "mypassword"  # Replace with your PostgreSQL password

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('Sample_Data_Site_Priority.csv')  # Replace with your CSV file path

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    host=host,
    port=port,
    dbname=dbname,
    user=user,
    password=password
)

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Get the column names from the DataFrame
columns = df.columns


# Create an SQL insert statement dynamically based on the columns
# insert_query = sql.SQL("INSERT INTO your_table ({}) VALUES ({})").format(
#     sql.SQL(',').join(map(sql.Identifier, columns)),
#     sql.SQL(',').join(sql.Placeholder() * len(columns))
# )

# # Iterate through the DataFrame rows and insert them into the PostgreSQL table
# for _, row in df.iterrows():
#     cursor.execute(insert_query, tuple(row))

# # Commit the transaction to save the changes
# conn.commit()

# # Close the cursor and connection
# cursor.close()
# conn.close()

# print("Data has been successfully inserted into the PostgreSQL table.")
