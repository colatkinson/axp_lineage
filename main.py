#!/bin/env python
import csv
import requests
from io import StringIO

url = 'https://docs.google.com/spreadsheet/ccc?key='\
      '1H77kqiz1R7xVBRXxjjMCqk_3AMF6P6qIMi6p2FEL_us&output=csv'

response = requests.get(url)
assert response.status_code == 200, 'Wrong status code'
buff = StringIO(response.content.decode("utf-8"))

classes = {}

reader = csv.reader(buff)
print("digraph brothers {")
first = True
for row in reader:
    if first:
        first = False
        continue
    classes.setdefault(row[2], []).append(row[1])
    print('\t"%s" -> "%s";' % (row[3], row[1]))

for key, val in classes.items():
    joined = ' '.join(['"' + item + '"' for item in val])
    print('\t{rank=same; %s;}' % joined)

print("}")
