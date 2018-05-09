#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  5 22:12:53 2018

@author: Nigel
"""
import numpy as np
import pandas as pd

DATASET_PATH = "/Users/Nigel/Desktop/Wash U/2018 Junior Spring/Research-ML/code/imputed.csv"
DATASET_ORIG = "/Users/Nigel/Desktop/Wash U/2018 Junior Spring/Research-ML/code/routefinal.csv"

dataraw = pd.read_csv(DATASET_PATH)
data_orig = pd.read_csv(DATASET_ORIG)

data_date = data_orig["datetime"]
data_day = data_orig["day"]
data_routeoption = data_orig["routeoption"]
data_joined = pd.concat([data_date, data_day], axis=1)

dataraw = pd.concat([data_joined,dataraw,data_routeoption],axis=1)

# temperature conversion from Kelvin(K) to Celcius()
for index,row in dataraw.iterrows():
    newtemp = float(row["temperature"]) - 273.15
    dataraw.set_value(index, 6, newtemp, True)
    
dataraw.to_csv("/Users/Nigel/Desktop/Wash U/2018 Junior Spring/Research-ML/code/routefinalimputed.csv",index=False)
