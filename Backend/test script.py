# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 17:52:59 2015

@author: millpa04
"""

# Adding Patty's python script directory to Windows' environmental variables 
import sys
sys.path.append('C:/Users/MillPa04/Documents/Python Scripts/')

# Importing Patty's python module
import toolbox

#Read in csv file by unicode
import unicodecsv
import pandas as pd

#################################
# Run and test Patty's algorithms
#################################

# Declare variables
#read in a NMP.csv file to practice from
IN_oct_data = 'C:/Users/MillPa04/Documents/Custom Analytics/NMP/Home zip/Home test/IN_demopanel_dataevents.csv'
with open(IN_oct_data, 'rb') as f:
    reader=unicodecsv.DictReader(f)
    IN_dataevents=list(reader)

#fix the data types
#create some functions to fix the different types of data
from datetime import datetime as dt

def parse_date(date):
    if date == '':
        return None
    else:
        return dt.strptime(date, '%m/%d/%Y %H:%M')
parse_date('10/01/2015 18:20')

def time_diff(rec1,rec2):
    date1 = parse_date(rec1['ENDTIMESTAMP'])
    date2 = parse_date(rec2['ENDTIMESTAMP'])
    return date1 - date2

print time_diff(IN_dataevents[0],IN_dataevents[1])

def parse_maybe_int(i):
    if i == '':
        return 0
    else:
        return int(i)

for IN_dataevent in IN_dataevents:
    IN_dataevent['ABNORMAL_TERM'] = parse_maybe_int(IN_dataevent['ABNORMAL_TERM'])  
    IN_dataevent['SETUP_SUCCESSFUL'] = parse_maybe_int(IN_dataevent['SETUP_SUCCESSFUL'])
    IN_dataevent['ENDTIMESTAMP'] = parse_date(IN_dataevent['ENDTIMESTAMP'])
  
print len(IN_dataevents[3])
#Run and test sum of two columns version 2 algorithm
print "The sum of abnormal term and setup successful is: %d" % (toolbox.sum_twocol(IN_dataevents[3],'ABNORMAL_TERM','SETUP_SUCCESSFUL'))

# Run and test algorithms
toolbox.distinct_count('ENDZIPCODE',IN_dataevents)

# Run and test sum of two numbers function
toolbox.sum_two(1,2)
#Run and test new function
toolbox.mult_two(2,5)

a=[1,2,3]
print toolbox.sum_list(a)

toolbox.my_average(a)
b=[2,3,4]
toolbox.sum_col(a,b)
toolbox.mult_col(a,b)


