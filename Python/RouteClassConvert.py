#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  2 23:59:37 2018

@author: Nigel
"""

import pandas as pd
import numpy as np

filename = '/Users/Nigel/Desktop/Wash U/2018 Junior Spring/Research-ML/code/routeraw.csv'

features = ["congestion", "warningcounts", "routeoption", "datetime", "day", "directions"]
data = pd.read_csv(filename, names=features)
#extracting routeoption column
routeoption = data.ix[:,['routeoption']]
routeoption = routeoption.values
RouteClassArray = []
#for index,val in routeoption.iterrows():
#    if not val in RouteClassArray:
#        RouteClassArray.append(val)
for val in routeoption:
    if not val in RouteClassArray:
        RouteClassArray.append(val)
print(RouteClassArray)
#if RouteClassA
rowindex =0
for index,row in data.iterrows():
#    print(row)
    for RouteClass in RouteClassArray:
#        print(RouteClass)
        if RouteClass == row["routeoption"]:
            data.set_value(rowindex, 2, RouteClassArray.index(RouteClass)+1, True)
    rowindex = rowindex+1

data.to_csv("/Users/Nigel/Desktop/Wash U/2018 Junior Spring/Research-ML/code/route.csv",index=False)
#dataformodify = pd.read_csv("/Users/Nigel/Desktop/Wash U/2018 Junior Spring/Research-ML/code/route.csv")
#mask = dataformodify.routeoption == 1
#column_name = 'routeoption'
#dataformodify.loc[mask, column_name] = 1
#
#mask2 = dataformodify.routeoption == 2
#mask3 = dataformodify.routeoption == 3
#mask4 = dataformodify.routeoption == 4
#mask5 = dataformodify.routeoption == 5
##mask6 = dataformodify.routeoption == 6
##mask7 = dataformodify.routeoption == 7
##mask8 = dataformodify.routeoption == 8
##mask9 = dataformodify.routeoption == 9
#
##convert the classes to 1,2,3
#column_name = 'routeoption'
#dataformodify.loc[mask2, column_name] = 1
#dataformodify.loc[mask3, column_name] = 2
#dataformodify.loc[mask5, column_name] = 2
##dataformodify.loc[mask6, column_name] = 1
##dataformodify.loc[mask7, column_name] = 1
#dataformodify.loc[mask4, column_name] = 3
##dataformodify.loc[mask8, column_name] = 3
##dataformodify.loc[mask9, column_name] = 3
#
#dataformodify.to_csv("/Users/Nigel/Desktop/Wash U/2018 Junior Spring/Research-ML/code/routemod.csv",index=False)