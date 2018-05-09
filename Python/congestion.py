#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  2 22:47:13 2018

@author: Nigel
"""
import pandas as pd
import numpy as np

filename = '/Users/Nigel/Desktop/Wash U/2018 Junior Spring/Research-ML/code/Chicago_Traffic_Tracker_-_Historical_Congestion_Estimates_by_Segment_-_2011-2018.csv'
route1 = [925,922,1038,1037,1036,1035,1034,1058,1059]
route2 = [925, 1286, 1288, 1259, 1258, 1059]

data_route1 = pd.read_csv(filename)
data_route1 = data_route1.ix[:,['TIME','SEGMENTID','SPEED']]
#segments for route1
r1seg1 = data_route1.loc[data_route1['SEGMENTID']== route1[0]]
r1seg1.to_csv("/Users/Nigel/Desktop/Wash U/2018 Junior Spring/Research-ML/code/r1seg1.csv",index=False)
r1seg2 = data_route1.loc[data_route1['SEGMENTID']== route1[1]]
r1seg2.to_csv("/Users/Nigel/Desktop/Wash U/2018 Junior Spring/Research-ML/code/r1seg2.csv",index=False)
r1seg3 = data_route1.loc[data_route1['SEGMENTID']== route1[2]]
r1seg3.to_csv("/Users/Nigel/Desktop/Wash U/2018 Junior Spring/Research-ML/code/r1seg3.csv",index=False)
r1seg4 = data_route1.loc[data_route1['SEGMENTID']== route1[3]]
r1seg4.to_csv("/Users/Nigel/Desktop/Wash U/2018 Junior Spring/Research-ML/code/r1seg4.csv",index=False)
r1seg5 = data_route1.loc[data_route1['SEGMENTID']== route1[4]]
r1seg5.to_csv("/Users/Nigel/Desktop/Wash U/2018 Junior Spring/Research-ML/code/r1seg5.csv",index=False)
r1seg6 = data_route1.loc[data_route1['SEGMENTID']== route1[5]]
r1seg6.to_csv("/Users/Nigel/Desktop/Wash U/2018 Junior Spring/Research-ML/code/r1seg6.csv",index=False)
r1seg7 = data_route1.loc[data_route1['SEGMENTID']== route1[6]]
r1seg7.to_csv("/Users/Nigel/Desktop/Wash U/2018 Junior Spring/Research-ML/code/r1seg7.csv",index=False)
r1seg8 = data_route1.loc[data_route1['SEGMENTID']== route1[7]]
r1seg8.to_csv("/Users/Nigel/Desktop/Wash U/2018 Junior Spring/Research-ML/code/r1seg8.csv",index=False)
r1seg9 = data_route1.loc[data_route1['SEGMENTID']== route1[8]]
r1seg9.to_csv("//Users/Nigel/Desktop/Wash U/2018 Junior Spring/Research-ML/code/r1seg9.csv",index=False)


#segments for route3
r2seg1 = data_route1.loc[data_route1['SEGMENTID']== route2[0]]
r2seg1.to_csv("/Users/Nigel/Desktop/Wash U/2018 Junior Spring/Research-ML/code/r2seg1.csv",index=False)
r2seg2 = data_route1.loc[data_route1['SEGMENTID']== route2[1]]
r2seg2.to_csv("/Users/Nigel/Desktop/Wash U/2018 Junior Spring/Research-ML/code/r2seg2.csv",index=False)
r2seg3 = data_route1.loc[data_route1['SEGMENTID']== route2[2]]
r2seg3.to_csv("/Users/Nigel/Desktop/Wash U/2018 Junior Spring/Research-ML/code/r2seg3.csv",index=False)
r2seg4 = data_route1.loc[data_route1['SEGMENTID']== route2[3]]
r2seg4.to_csv("/Users/Nigel/Desktop/Wash U/2018 Junior Spring/Research-ML/code/r2seg4.csv",index=False)
r2seg5 = data_route1.loc[data_route1['SEGMENTID']== route2[4]]
r2seg5.to_csv("/Users/Nigel/Desktop/Wash U/2018 Junior Spring/Research-ML/code/r2seg5.csv",index=False)
r2seg6 = data_route1.loc[data_route1['SEGMENTID']== route2[5]]
r2seg6.to_csv("/Users/Nigel/Desktop/Wash U/2018 Junior Spring/Research-ML/code/r2seg6.csv",index=False)