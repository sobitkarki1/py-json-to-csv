import json
import csv

# Load JSON data from the file
with open('listfile.txt', 'r') as json_file:
    data = json.load(json_file)

# Define the field names for CSV
field_names = ['l', 'v', 'd']

# Write data to CSV file
with open('data.csv', 'w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(data)
