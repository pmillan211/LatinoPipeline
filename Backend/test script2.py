# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 09:25:04 2015

@author: millpa04
"""

#Udacity - Intro to Data Analysis
#Lession 1 Data Analysis Process

# If you run this cell, you should see a scatter plot of the function y = x^2

%pylab inline
import matplotlib.pyplot as plt

xs = range(-30, 31)
ys = [x ** 2 for x in xs]

plt.scatter(xs, ys)

import numpy as np
a = np.array([[1,2,3],[3,4,5]])
b=np.array(range(0,10))
b

# If you run this cell, you should see the values displayed as a table.

# Pandas is a software library for data manipulation and analysis. You'll learn to use it later in this course.
import pandas as pd

df = pd.DataFrame({'a': [2, 4, 6, 8], 'b': [1, 3, 5, 7]})
df


a = [1,2,3]
for i in a:
    print i+1
    