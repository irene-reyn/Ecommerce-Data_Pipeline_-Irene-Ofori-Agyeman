
# E-commerce Data Pipeline

## Overview

The E-commerce Data Pipeline project aims to design and implement a robust data pipeline tailored for a large-scale e-commerce platform. The pipeline incorporates various components to handle complexities such as data schema evolution, incremental updates, data transformation, scalability, fault tolerance, and efficient data storage.

## Cleanup Analysis

The cleanup analysis phase involved assessing the raw datasets to understand their structure and prepare them for further processing. Here's an overview of the process and results:

- **Script**: The cleanup analysis script was developed to inspect the structure of the datasets and perform necessary cleaning tasks.
- **Datasets Evaluated**:
  - Market 1 Customers.json
  - Market 2 Customers.json
  - Market 1 Orders.csv
  - Market 2 Orders.csv
  - Market 1 Deliveries.csv
  - Market 2 Deliveries.csv
- **Results**: The script successfully read each dataset, extracted column headers, and displayed them. This provided insights into the structure of the data, enabling further processing.

## Main Script

The main script focuses on implementing the core functionalities of the data pipeline. Here's an overview of the process and results:

- **Spark Configuration**: The script configures the Spark environment for processing large datasets.
- **Data Ingestion**: Utilizing Spark, the script reads data from CSV files and loads them into Spark DataFrames.
- **Spark SQL Operations**: DataFrames are registered as temporary views for performing SQL queries.
- **Data Persistence**: Processed data is persisted to a PostgreSQL database for storage and future retrieval.
- **Results**: The pipeline successfully ingests, processes, and stores the e-commerce data, ensuring its availability for analytics and reporting purposes.

## Requirements

The project relies on the following dependencies to function properly:
[requirements.txt](https://github.com/irene-reyn/Ecommerce-Data_Pipeline_-Irene-Ofori-Agyeman/blob/main/requirements.txt)

## License

This project is licensed under the MIT License. 


