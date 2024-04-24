import pandas as pd
import os

# Define the path to the directory containing the consolidated data file
consolidated_data_folder = "transformed_data"

# Define the file name of the consolidated data
consolidated_file_name = "all_markets_data.csv"

# Define the output folder for the modified data
output_folder = "data"

# Define the output file name
output_file_name = "markets_data.csv"

# Read the consolidated data file
consolidated_data = pd.read_csv(os.path.join(consolidated_data_folder, consolidated_file_name))

# Define the columns that may have decimal values
columns_to_check = ['deliveries_order_id', 'customer_data_customer_id', 'orders_order_id', 'orders_transaction_id', 'orders_customer_id', 'orders_merchant_id']

# Remove '.0' from the values in the specified columns
for column in columns_to_check:
    consolidated_data[column] = consolidated_data[column].astype(str).str.replace(r'\.0', '', regex=True)

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Define the output file path
output_file_path = os.path.join(output_folder, output_file_name)

# Save the modified DataFrame to a new CSV file
consolidated_data.to_csv(output_file_path, index=False)

print(f"Modified data saved in '{output_file_path}'")
