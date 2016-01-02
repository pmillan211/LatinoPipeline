# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 17:33:18 2015

@author: millpa04
"""

# Extra Modules
import json

#create a function that takes two independent columns and multiplies them into a new column
def mult_col(col1,col2):
    col3=[]
    for x,y in zip(col1,col2):
        col3.append(x*y)
    return col3

#create a function that takes two columns within the same data set and returns a new column
#def new_col_mult(var1,var2,dataset):
#    var3=[]
#    for x,y in dataset:
#        var3.append(x[var1]*y[var2])
#    return var3

#create a function that calc the distinct count of any variable

def distinct_count(var,dataset):
    unique_count=set()
    for row in dataset:
        unique_count.add(row[var])
    return len(unique_count)

#create a function that adds two numbers
def sum_two(var1, var2):
    total_sum = var1+var2
    return total_sum

#create a function that multiply two numbers
def mult_two(var1,var2):
    return var1*var2
 
def sum_list(list1):
    #step1 set variable to zero
    #step2 add each variable to another
    total_sum=0
    for i in list1:
        total_sum = total_sum + i
    return total_sum

#create a function that calc the average of a list of numbers
def my_average(list1):
    #step 1 sum all numbers in a list
    #step 2 count of numbers in a list
    #step 3 divide total sum by count
    return sum_list(list1)/len(list1)

#create a function that would take two columns and outputs one column that is the sum of the two columns
#independent lists
def sum_col(col1,col2):
    col3 = []
    for x,y in zip(col1,col2): #zip function allows you iterate through multiple lists
        col3.append(x+y)
    return col3

def parse_date(date):
    if date == '':
        return None
    else:
        return dt.strptime(date, '%m/%d/%Y %H:%M')

def parse_maybe_int(i):
    if i == '':
        return 0
    else:
        return int(i)

def time_diff(rec1,rec2, field1):
    date1 = parse_date(rec1[field1])
    date2 = parse_date(rec2[field1])
    return date1 + date2

#print time_diff(IN_dataevents[0],IN_dataevents[1],'ENDTIMESTAMP')

def diff_within_rec(rec,field1,field2):
    intField1 = parse_maybe_int(rec[field1])
    intField2 = parse_maybe_int(rec[field2])
    return intField1 - intField2

def sum_twocol(rec,field1,field2):
    intField1 = parse_maybe_int(rec[field1])
    intField2 = parse_maybe_int(rec[field2])
    return intField1 + intField2



# -----------------------------------------------------------------------
# Website Back End Tools
# -----------------------------------------------------------------------

def updateField(sFileData_, sUserProf_, sField_):

    # Find the string between the tokens
    left, leftToken, rest = sFileData_.partition("<!--" + sField_ + "-->")
    block, rightToken, right = rest.partition("<!--/" + sField_ + "-->")
    
    # Replace the old name with the new
    jsonUserProf = json.loads(sUserProf_)
    sFileData_ = left + leftToken + "<p>" + jsonUserProf[ sField_ ] + "</p>" + rightToken + right

    return sFileData_

def updateFrontEnd(sFrontEndFullPath_, sUserProf_):
    
    # Open the front end and store it in a temp variable
    f = open(sFrontEndFullPath_, 'r+')
    sFileData = f.read()
    f.close()
    
    # Update profile
    print sFileData
    sFileData_ = updateField(sFileData, sUserProf_, "NAME")
    sFileData_ = updateField(sFileData_, sUserProf_, "EXPERIENCE")
    sFileData_ = updateField(sFileData_, sUserProf_, "EDUCATION")    
    print sFileData_

    # When I write, I don't print the sFileData_ string, I only print name1
    f = open(sFrontEndFullPath_, 'wb')
    f.write(sFileData_)
    f.close()