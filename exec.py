import csv
import json
input_file_name = "data.json"
output_file_name = "data.csv"
with open(input_file_name, "r", encoding="utf-8", newline="") as input_file, \
        open(output_file_name, "w", encoding="utf-8", newline="") as output_file:
    data = json.load(input_file)
        
    csvwriter = csv.writer(output_file, delimiter=',', quoting=csv.QUOTE_NONE)
    keys = list(data[0].keys())
    csvwriter.writerow(keys)
    print(keys)
    for line in data:
        print(line)
        form = {}
        for key in keys:
            form[key] = line[key] if key in line else None
        csvwriter.writerow(form.values())
