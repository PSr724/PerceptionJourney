import csv
import os

# Get the absolute path of the directory containing this script
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'data.csv')

with open(file_path, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    cone_data = list(reader)

    print(cone_data)