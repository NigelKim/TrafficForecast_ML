#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  4 23:44:02 2018

@author: dohoonkim
"""

import pandas as pd
import numpy as np
import datetime
from datetime import timedelta

r1seg1 = pd.read_csv('/Users/dohoonkim/Desktop/Traffic/route3/r2seg6.csv')
filename = '/Users/dohoonkim/Desktop/Traffic/plsroute2.csv'

data = pd.read_csv(filename)

rowindex = 0
for index,row in data.iterrows():
    datetimevar = row["datetime"]
    if datetimevar.find('/') == 1:     #check if month is 1 digit
        datetimevar = "0"+datetimevar
    if datetimevar.rfind('/') == 4:    #check if date is 1 digit
        datetimevar = datetimevar[:3]+"0"+datetimevar[3:]
    if datetimevar.rfind(':') == 12:     #check if hour is 1 digit
        datetimevar = datetimevar[:11] + "0" + datetimevar[11:]
        
    data.set_value(rowindex, 3, datetimevar[:10], True) #only compare the date
    rowindex = rowindex+1

rowforseg = 0



for index,row in r1seg1.iterrows():
    date = row["TIME"]
    r1seg1.set_value(rowforseg, 0, date[:10],True)
    rowforseg = rowforseg+1
    

r1seg1ExistDate = r1seg1.drop_duplicates(['TIME'],keep='first')
rowforupdate = 0
r1seg1ExistDate 
listtemp = []
for index,row in r1seg1ExistDate.iterrows():
    uniquedate = row["TIME"]
    newr1seg1 = r1seg1[r1seg1["TIME"]==uniquedate]
    newr1seg1 = newr1seg1[0:5]
    temp = []
    for rowin, rowi in newr1seg1.iterrows():
        if rowi["SPEED"] != -1:
            temp.append(rowi["SPEED"])
    average = np.mean(temp)
#    average = newr1seg1["SPEED"].mean()
    listtemp.append(average)
    rowforupdate = rowforupdate+1

r1seg1ExistDate['averagespeed'] = listtemp;
#for index,row in r1seg1ExistDate.iterrows():
#    

r1seg1ExistDate.to_csv("uniqueR2Seg6.csv",index=False)
#data[(~data.)]
    