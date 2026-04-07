
# Documentation - Excel_parser.py (EN)

## Description
This script automatically processes CSV files containing client data. It detects the latest `clients_*.csv` file, opens and sorts the data, and exports it to a well-formatted Excel file using a styled table.

## Main Features
- Automatically detects the most recent CSV file
- Reads and sorts data by date
- Cleans and groups data by client
- Generates a structured Excel file (OpenPyXL)

## Libraries Used
- `csv`, `os`, `glob`, `datetime`, `re`
- `openpyxl` for Excel file generation

## Output
A `clients_traités.xlsx` file is created with clean, sorted data.
