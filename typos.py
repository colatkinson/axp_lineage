#!/bin/env python
import csv
import requests
from io import StringIO
import difflib

url = 'https://docs.google.com/spreadsheet/ccc?key='\
      '1H77kqiz1R7xVBRXxjjMCqk_3AMF6P6qIMi6p2FEL_us&output=csv'

response = requests.get(url)
assert response.status_code == 200, 'Wrong status code'
buff = StringIO(response.content.decode("utf-8"))

classes = {}

reader = csv.reader(buff)

rows = list(reader)
del rows[0]

bros = [row[1] for row in rows]
bigs = [row[3] for row in rows]

for big in bigs:
    if big in bros or big == '':
        continue
    print("Big %s: %s" % (big, difflib.get_close_matches(big, bros)))

