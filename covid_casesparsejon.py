import json
import csv

with open('covid_cases_json', 'r') as json_file:
    num_json = json.load(json_file)

data_covid = num_json['records']

covid_cases = open('covid_cases.csv', 'w')

write_csv = csv.writer(covid_cases)

head1 = dateRep.keys()
head2 = countriesAndTerritories.keys()
head3 = deaths.keys()
head4 = cases.keys()

write_csv.writerow(head1)
write_csv.writerow(head2)
write_csv.writerow(head3)
write_csv.writerow(head4)

write_csv.writerow(head1.values())
write_csv.writerow(head2.values())
write_csv.writerow(head3.values())
write_csv.writerow(head4.values())

data_covid.close()


