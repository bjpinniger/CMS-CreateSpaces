import requests
import csv
from cms import CMS

with open('SpaceNames.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        name = row['SpaceName']
        PIN = row['PIN']
        coSpace_id = CMS.createSpace(name, PIN, '')
        print(name + " has been created. Space id: " + coSpace_id)
 
csvfile.close()
