#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 01:14:39 2018

@author: Nigel
"""

import pandas as pd
import numpy as np
import datetime
from datetime import timedelta

filename = '/Users/Nigel/Desktop/Wash U/2018 Junior Spring/Research-ML/code/route.csv'
weatherpath = '/Users/Nigel/Desktop/Wash U/2018 Junior Spring/Research-ML/code/weatherfinal.csv'

weatherfeatures = ["datetime", "weather", "temperature", "windspeed"]
#segmentfeatures = ["TIME", "SEGMENTID", "SPEED"]
data = pd.read_csv(filename)

con_df = pd.DataFrame({'congestionSpeed': []})
data = data.append(con_df)
seg1 = pd.read_csv("/Users/Nigel/Desktop/Wash U/2018 Junior Spring/Research-ML/code/uniqueR1Seg1.csv")
nanflag = 0
#timeEnum = []
#speedsums = []
#counts = []
#speedavg = []
#con_df = pd.DataFrame({'congestionSpeed': []})
#
#for index, row in seg1.iterrows():
#    if not row["TIME"] in timeEnum:
#        timeEnum.append(row["TIME"])
#        speedsums.append(row["speed"])
#        counts.append(1)
#    else:
#        idx = timeEnum.find(row["TIME"])
#        speedsums[idx] = speedsums[idx]+row["speed"]
#        counts[idx] = counts[idx]+1
#for x in range(0, len(timeEnum)):
#    speedavg.append(speedsums[x]/counts[x])
#    
#rowindex = 0
for index,row in data.iterrows():
#    print(row)\
    datetimevar = row["datetime"]     #6/1/14 17:00
    if datetimevar.find('/') == 1:     #check if month is 1 digit
        datetimevar = "0"+datetimevar
    if datetimevar.rfind('/') == 4:    #check if date is 1 digit
        datetimevar = datetimevar[:3]+"0"+datetimevar[3:]
#        print(datetimevar)
    if datetimevar.rfind(':') == 12:     #check if hour is 1 digit
        datetimevar = datetimevar[:11] + "0" + datetimevar[11:]
        
    datetimevar = datetimevar[:int(datetimevar.rfind('/'))+1] + datetimevar[(int(datetimevar.rfind('/'))+1):]
    data.set_value(index, 2, datetimevar, True)
    
    if datetimevar[3:5] != '01':
#                print(datetimevar[3:5])
#            daystring = segtimerow["TIME"][3:5]
#            segtime = segtimerow["TIME"][:3]+str(int(daystring)-1)+segtimerow["TIME"][5:]
#            print(datetimevar)
#        print(datetimevar)
        datetimevar = datetimevar[:3]+str(int(datetimevar[3:5])-1)+datetimevar[5:]
    else:
        today = datetime.datetime(int(datetimevar[datetimevar.rfind('/')+1:datetimevar.rfind('/')+5]), int(datetimevar[:2]), int(datetimevar[datetimevar.find('/')+1:datetimevar.find('/')+3]))
        yesterday = today - timedelta(days=1)
        day = str(yesterday.day)
#            segtime = segtimerow["TIME"][:3]+day+segtimerow["TIME"][5:]
        datetimevar = datetimevar[:3]+day+datetimevar[5:]
#    print(datetimevar)
    for ix,segtimerow in seg1.iterrows():
        
        
#        print(segtimerow["TIME"])
#        print(datetimevar[:10])
        if(segtimerow["TIME"] == datetimevar[:10]):
            nanflag = 1
#            print(segtime)
#            print(datetimevar[:10])
            # now, date time will look like 06/01/2014 17:00
            today = datetime.datetime(int(datetimevar[datetimevar.rfind('/')+1:datetimevar.rfind('/')+5]), int(datetimevar[:2]), int(datetimevar[datetimevar.find('/')+1:datetimevar.find('/')+3]))
            yesterday = today - timedelta(days=1)
            
            
            
            if row["routeoption"] == 1:
#                print("1")
#                month = str(yesterday.month)
#                day = str(yesterday.day)
#                year = str(yesterday.year)
#                if yesterday.month < 10:
#                    month = "0"+month
#                if yesterday.day < 10:
#                    day = "0"+day
                month = segtimerow["TIME"][0:2]
                day = segtimerow["TIME"][3:5]
                year = segtimerow["TIME"][6:10]
                    
                seg1 = pd.read_csv("/Users/Nigel/Desktop/Wash U/2018 Junior Spring/Research-ML/code/uniqueR1Seg1.csv")
#                print(month+'/'+day+'/'+year)
                seg1row = seg1[seg1.TIME == month+'/'+day+'/'+year]  #02/02/2013 11:52:32 PM
                seg1speed = seg1row['averagespeed'].astype(float)
                
                seg2 = pd.read_csv("/Users/Nigel/Desktop/Wash U/2018 Junior Spring/Research-ML/code/uniqueR1Seg2.csv")
                seg2row = seg2[seg2.TIME == month+'/'+day+'/'+year]  #02/02/2013 11:52:32 PM
                seg2speed = seg2row['averagespeed'].astype(float)
                
                seg3 = pd.read_csv("/Users/Nigel/Desktop/Wash U/2018 Junior Spring/Research-ML/code/uniqueR1Seg3.csv")
                seg3row = seg3[seg3.TIME == month+'/'+day+'/'+year]  #02/02/2013 11:52:32 PM
                seg3speed = seg3row['averagespeed'].astype(float)
                
                seg4 = pd.read_csv("/Users/Nigel/Desktop/Wash U/2018 Junior Spring/Research-ML/code/uniqueR1Seg4.csv")
                seg4row = seg4[seg4.TIME == month+'/'+day+'/'+year]  #02/02/2013 11:52:32 PM
                seg4speed = seg4row['averagespeed'].astype(float)
                
                seg5 = pd.read_csv("/Users/Nigel/Desktop/Wash U/2018 Junior Spring/Research-ML/code/uniqueR1Seg5.csv")
                seg5row = seg5[seg5.TIME == month+'/'+day+'/'+year]  #02/02/2013 11:52:32 PM
                seg5speed = seg5row['averagespeed'].astype(float)
                
                seg6 = pd.read_csv("/Users/Nigel/Desktop/Wash U/2018 Junior Spring/Research-ML/code/uniqueR1Seg6.csv")
                seg6row = seg6[seg6.TIME == month+'/'+day+'/'+year]  #02/02/2013 11:52:32 PM
                seg6speed = seg6row['averagespeed'].astype(float)
                
                seg7 = pd.read_csv("/Users/Nigel/Desktop/Wash U/2018 Junior Spring/Research-ML/code/uniqueR1Seg7.csv")
                seg7row = seg7[seg7.TIME == month+'/'+day+'/'+year]  #02/02/2013 11:52:32 PM
                seg7speed = seg7row['averagespeed'].astype(float)
                
                seg8 = pd.read_csv("/Users/Nigel/Desktop/Wash U/2018 Junior Spring/Research-ML/code/uniqueR1Seg8.csv")
                seg8row = seg8[seg8.TIME == month+'/'+day+'/'+year]  #02/02/2013 11:52:32 PM
                seg8speed = seg8row['averagespeed'].astype(float)
                
                seg9 = pd.read_csv("/Users/Nigel/Desktop/Wash U/2018 Junior Spring/Research-ML/code/uniqueR1Seg9.csv")
                seg9row = seg9[seg9.TIME == month+'/'+day+'/'+year]  #02/02/2013 11:52:32 PM
                seg9speed = seg9row['averagespeed'].astype(float)
#                print(type(seg9speed))
#                print(seg9speed)
                seg1speed.add(seg2speed, fill_value=0).add(seg3speed, fill_value=0).add(seg4speed, fill_value=0).add(seg5speed, fill_value=0).add(seg6speed, fill_value=0).add(seg7speed, fill_value=0).add(seg8speed, fill_value=0).add(seg9speed, fill_value=0)
                
                avg_speed = (seg1speed.sum()/9)
#                print(type(avg_speed))
                data.set_value(index, 1, avg_speed, True)
                break
                
            elif row["routeoption"] == 2:
#                print("2")
#                month = str(yesterday.month)
#                day = str(yesterday.day)
#                year = str(yesterday.year)
#                if yesterday.month < 10:
#                    month = "0"+month
#                if yesterday.day < 10:
#                    day = "0"+day
                month = segtimerow["TIME"][0:2]
                day = segtimerow["TIME"][3:5]
                year = segtimerow["TIME"][6:10]
                    
                seg1 = pd.read_csv("/Users/Nigel/Desktop/Wash U/2018 Junior Spring/Research-ML/code/uniqueR2Seg1.csv")
                seg1row = seg1[seg1.TIME == month+'/'+day+'/'+year]  #02/02/2013 11:52:32 PM
                seg1speed = seg1row['averagespeed'].astype(float)
                
                seg2 = pd.read_csv("/Users/Nigel/Desktop/Wash U/2018 Junior Spring/Research-ML/code/uniqueR2Seg2.csv")
                seg2row = seg2[seg2.TIME == month+'/'+day+'/'+year]  #02/02/2013 11:52:32 PM
                seg2speed = seg2row['averagespeed'].astype(float)
                
                seg3 = pd.read_csv("/Users/Nigel/Desktop/Wash U/2018 Junior Spring/Research-ML/code/uniqueR2Seg3.csv")
                seg3row = seg3[seg3.TIME == month+'/'+day+'/'+year]  #02/02/2013 11:52:32 PM
                seg3speed = seg3row['averagespeed'].astype(float)
                
                seg4 = pd.read_csv("/Users/Nigel/Desktop/Wash U/2018 Junior Spring/Research-ML/code/uniqueR2Seg4.csv")
                seg4row = seg4[seg4.TIME == month+'/'+day+'/'+year]  #02/02/2013 11:52:32 PM
                seg4speed = seg4row['averagespeed'].astype(float)
                
                seg5 = pd.read_csv("/Users/Nigel/Desktop/Wash U/2018 Junior Spring/Research-ML/code/uniqueR2Seg4.csv")
                seg5row = seg5[seg5.TIME == month+'/'+day+'/'+year]  #02/02/2013 11:52:32 PM
                seg5speed = seg5row['averagespeed'].astype(float)
                
                seg6 = pd.read_csv("/Users/Nigel/Desktop/Wash U/2018 Junior Spring/Research-ML/code/uniqueR2Seg5.csv")
                seg6row = seg6[seg6.TIME == month+'/'+day+'/'+year]  #02/02/2013 11:52:32 PM
                seg6speed = seg6row['averagespeed'].astype(float)
                
                seg1speed.add(seg2speed, fill_value=0).add(seg3speed, fill_value=0).add(seg4speed, fill_value=0).add(seg5speed, fill_value=0).add(seg6speed, fill_value=0)

                avg_speed = (seg1speed.sum()/6)
#                print(type(avg_speed))
                
                data.set_value(index, 1, avg_speed, True)
                break
#        else:
#    if nanflag == 0:
#        data.set_value(index, 1, 0, True)
#        rowindex = rowindex+1

weatherfinal = pd.read_csv(weatherpath, names=weatherfeatures)
#cols = ['weather', 'temperature', 'windspeed']
#weatherdata = weatherfinal[cols]
#data = pd.concat([data, weatherdata], axis=1, join_axes=[data.index])
data = data.merge(weatherfinal, on="datetime", how="left")

cols = ['datetime', 'day', 'congestion', 'congestionSpeed', 'warningcounts', 'weather', 'temperature', 'windspeed', 'routeoption']
data = data.ix[:, cols]

data.to_csv("/Users/Nigel/Desktop/Wash U/2018 Junior Spring/Research-ML/code/routefinal.csv",index=False)



                