# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 14:48:06 2015

@author: millpa04
"""

#read in a NMP.csv file to practice from
import unicodecsv
IN_oct_data = 'C:/Users/MillPa04/Documents/Custom Analytics/NMP/Home zip/Home test/IN_demopanel_dataevents.csv'
with open(IN_oct_data, 'rb') as f:
    reader=unicodecsv.DictReader(f)
    IN_dataevents=list(reader)
IN_dataevents[1]

#fix the data types
#create some functions to fix the different types of data
from datetime import datetime as dt

def parse_date(date):
    if date == '':
        return None
    else:
        return dt.strptime(date, '%m/%d/%Y %H:%M')
parse_date('10/01/2015 18:20')

def parse_maybe_int(i):
    if i == '':
        return 0
    else:
        return int(i)


for IN_dataevent in IN_dataevents:
    IN_dataevent['ABNORMAL_TERM'] = parse_maybe_int(IN_dataevent['ABNORMAL_TERM'])  
    IN_dataevent['SETUP_SUCCESSFUL'] = parse_maybe_int(IN_dataevent['SETUP_SUCCESSFUL'])
    IN_dataevent['ENDTIMESTAMP'] = parse_date(IN_dataevent['ENDTIMESTAMP'])
  
IN_dataevents[0]


#get the total number of rows in this data set
len(IN_dataevents)
#counting the number of unique zipcode
unique_number_zips=set()
for IN_dataevent in IN_dataevents:
    unique_number_zips.add(IN_dataevent['ENDZIPCODE'])
len(unique_number_zips)

#create a function that calc the distinct count of any variable

def distinct_count(var):
    unique_count=set()
    for IN_dataevent in IN_dataevents:
        unique_count.add(IN_dataevent[var])
    return len(unique_count)
        
print distinct_count('ENDZIPCODE')
distinct_count('PANELISTID')



    