import json
import csv
from os import write

with open('covid_cases.json', 'r') as json_file:
    num_json = json.load(json_file)

data_covid = num_json['records']

covid_cases = open('covid_cases.csv', 'w')

write_csv = csv.writer(covid_cases)

count = 0
for i in data_covid:
    if count == 0:
        header = i.keys()
        write_csv.writerow(header)

    write_csv.writerow(i.values())

covid_cases.close


