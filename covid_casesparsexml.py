import xml.etree.cElementTree as et

tree = et.parse("covid_cases_xml.xml")
root = tree.getroot()
dateRep = []
cases = []
deaths = []

for dateRep in root.iter('dateRep'):
    dateRep.append(dateRep.text)

for continent in root.iter('continentExp'):
    continentExp.append(continent.text)

print(dateRep)
print(continentExp)