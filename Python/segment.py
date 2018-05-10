#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  2 22:03:08 2018

@author: dohoonkim
"""

import pandas as pd
import numpy as np

filename = 'chicagosegments2.csv'
route1 = [925,922,1038,1037,1036,1035,1034,1058,105]
route3 = [925, 1286, 1288, 1259, 1258, 1059]

data_route1 = pd.read_csv(filename)
data_route1 = data_route1.ix[:,['TIME','SEGMENTID','SPEED']]
#segments for route1
r1seg1 = data_route1.loc[data_route1['SEGMENTID']== route1[0]]
r1seg1.to_csv("/Users/dohoonkim/Desktop/Traffic/route1/r1seg1.csv",index=False)
r1seg2 = data_route1.loc[data_route1['SEGMENTID']== route1[1]]
r1seg2.to_csv("/Users/dohoonkim/Desktop/Traffic/route1/r1seg2.csv",index=False)
r1seg3 = data_route1.loc[data_route1['SEGMENTID']== route1[2]]
r1seg3.to_csv("/Users/dohoonkim/Desktop/Traffic/route1/r1seg3.csv",index=False)
r1seg4 = data_route1.loc[data_route1['SEGMENTID']== route1[3]]
r1seg4.to_csv("/Users/dohoonkim/Desktop/Traffic/route1/r1seg4.csv",index=False)
r1seg5 = data_route1.loc[data_route1['SEGMENTID']== route1[4]]
r1seg5.to_csv("/Users/dohoonkim/Desktop/Traffic/route1/r1seg5.csv",index=False)
r1seg6 = data_route1.loc[data_route1['SEGMENTID']== route1[5]]
r1seg6.to_csv("/Users/dohoonkim/Desktop/Traffic/route1/r1seg6.csv",index=False)
r1seg7 = data_route1.loc[data_route1['SEGMENTID']== route1[6]]
r1seg7.to_csv("/Users/dohoonkim/Desktop/Traffic/route1/r1seg7.csv",index=False)
r1seg8 = data_route1.loc[data_route1['SEGMENTID']== route1[7]]
r1seg8.to_csv("/Users/dohoonkim/Desktop/Traffic/route1/r1seg8.csv",index=False)
r1seg9 = data_route1.loc[data_route1['SEGMENTID']== route1[8]]
r1seg9.to_csv("/Users/dohoonkim/Desktop/Traffic/route1/r1seg9.csv",index=False)


#segments for route3
r2seg1 = data_route1.loc[data_route1['SEGMENTID']== route3[0]]
r2seg1.to_csv("/Users/dohoonkim/Desktop/Traffic/route3/r2seg1.csv",index=False)
r2seg2 = data_route1.loc[data_route1['SEGMENTID']== route3[1]]
r2seg2.to_csv("/Users/dohoonkim/Desktop/Traffic/route3/r2seg2.csv",index=False)
r2seg3 = data_route1.loc[data_route1['SEGMENTID']== route3[2]]
r2seg3.to_csv("/Users/dohoonkim/Desktop/Traffic/route3/r2seg3.csv",index=False)
r2seg4 = data_route1.loc[data_route1['SEGMENTID']== route3[3]]
r2seg4.to_csv("/Users/dohoonkim/Desktop/Traffic/route3/r2seg4.csv",index=False)
r2seg5 = data_route1.loc[data_route1['SEGMENTID']== route3[4]]
r2seg5.to_csv("/Users/dohoonkim/Desktop/Traffic/route3/r2seg5.csv",index=False)
r2seg6 = data_route1.loc[data_route1['SEGMENTID']== route3[5]]
r2seg6.to_csv("/Users/dohoonkim/Desktop/Traffic/route3/r2seg6.csv",index=False)