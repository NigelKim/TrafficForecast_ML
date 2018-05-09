#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 22:15:31 2018

@author: Nigel
"""

import numpy as np
import pandas as pd
import sys
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import datetime
from datetime import timedelta
from sklearn.model_selection import cross_val_score

import sklearn.gaussian_process as gp
from sklearn import tree
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import gaussian_process
from sklearn import svm
from sklearn.gaussian_process.kernels import (RBF, Matern, RationalQuadratic,
                                              ExpSineSquared, DotProduct,
                                              ConstantKernel)
from sklearn.naive_bayes import GaussianNB
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn import linear_model
from sklearn.ensemble import AdaBoostClassifier
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc
import time as time
import math as math

# ======================IF RUN IN TERMINAL=====================================
#def validate_cmdline_args(nargs, msg):
#    if len(sys.argv) < nargs:
#        print(msg)
#        sys.exit(1)
#        
#validate_cmdline_args(3,'Usage: python maintemplate.py <DATASET_PATH> <ex: Mon or Tue>')
#DATASET_PATH = sys.argv[1]
#if len(sys.argv[2]) == 3:
#    dayofweek = sys.argv[2]
#else:
#    sys.exit(1)
# =============================================================================

#from fancyimpute import KNN
# Naive Bayes 1 : categorical features ----------------------------------------
#DATASET_PATH = "/Users/Nigel/Desktop/Wash U/2018 Junior Spring/Research-ML/code/routefinal.csv"
#data_features = ["congestionSpeed","warningcounts","temperature","windspeed","weather_cat","Heavy"]
# -----------------------------------------------------------------------------

# Naive Bayes 2: Multiple Binary Features--------------------------------------
#DATASET_PATH = "/Users/Nigel/Desktop/Wash U/2018 Junior Spring/Research-ML/code/routefinal.csv"
##data_features = ["congestion","congestionSpeed","warningcounts","weather","temperature","windspeed"]
#data_features = ["congestionSpeed","warningcounts","temperature","windspeed","Clouds","Clear","Mist","Rain","Snow","Drizzle","Haze","Heavy"]
# -----------------------------------------------------------------------------

# ML 3 : MICE version features ------------------------------------------------
DATASET_PATH = "/Users/Nigel/Desktop/Wash U/2018 Junior Spring/Research-ML/code/routefinalimputed.csv"
data_features = ["congestion", "congestionSpeed", "warningcounts", "weather", "temperature", "windspeed"]
# -----------------------------------------------------------------------------

#DATASET_PATH = "/Users/Nigel/Desktop/Wash U/2018 Junior Spring/Research-ML/code/routefinalimputed.csv"

data = pd.read_csv(DATASET_PATH)



## Naive Bayes 1 & 2  ----------------------------------------------------------
#
##data imputation
##Try with mean imputation for numerical features
##we can choose strategy: mean, median, most_frequent
#imputer = Imputer(missing_values=np.nan, strategy='mean', axis=0)
#data[["congestionSpeed"]] = imputer.fit_transform(data[["congestionSpeed"]])
#data[["warningcounts"]] = imputer.fit_transform(data[["warningcounts"]])
#data[["temperature"]] = imputer.fit_transform(data[["temperature"]])
#data[["windspeed"]] = imputer.fit_transform(data[["windspeed"]])
#
##data imputation for categorical feature: weather, congestion
##Tried most frequent method for filling nan
##make dummy variables, count and sort descending:
#most_common = pd.get_dummies(data["weather"]).sum().sort_values(ascending=False).index[0] 
#
#def replace_most_common(feat):
#    if pd.isnull(feat):
#        return most_common
#    else:
#        return feat
#
#data["weather"] = data["weather"].map(replace_most_common)
#
#
## Naive Bayes 1 : categorical features ----------------------------------------
#data["weather"] = data["weather"].astype('category')
##add weather categories as label numbers: -1 for Nan, 0, 1, ...
#data["weather_cat"] = data["weather"].cat.codes
## -----------------------------------------------------------------------------
#
### Naive Bayes 2: Multiple Binary Features -------------------------------------
###convert categorical feature weather into multi binary features
###find unique classes
##for weather_class in data.weather.unique():
##    data[weather_class] = (data.weather==weather_class).astype(float)
##    data[weather_class] = data[weather_class].astype(np.float64)
### -----------------------------------------------------------------------------
#
#for congestion_class in data.congestion.unique():
#    data[congestion_class] = (data.congestion==congestion_class).astype(float)
#    data[congestion_class] = data[congestion_class].astype(np.float64)
#
#data = data.drop(['congestion','weather'],axis=1)
#
##reordering columns
#cols = data.columns.tolist()
##print(cols)
#
## Naive Bayes 1 : categorical features ----------------------------------------
#cols = cols[:6]+cols[7:]+[cols[6]]
##print(cols)
#
## -----------------------------------------------------------------------------
## Naive Bayes 2: Multiple Binary Features -------------------------------------
##cols = cols[:6] + cols[7:17] + [cols[6]]
## -----------------------------------------------------------------------------
##print(cols)
#data = data[cols]
##-------------------------------end of Naive Bayes 1 & 2-----------------------



#-----------------------------ML-----------------------------------------------
#normalize the dataset
#normalized_data = StandardScaler().fit_transform(data[data_features])

# if predict by day of the week 
dataDay = data[data.day == 'Mon']  
train_x, test_x, train_y, test_y = train_test_split(dataDay[data_features],dataDay["routeoption"], train_size=0.2)

accuracy = 0
cvmean = 0
cvstd = 0
#cvs = []
y_score=[]
for i in range(0,10):
##    ML 1 : Naive Bayes ------------------------------------------------------
#    clf = GaussianNB()
##    ML 2 : Logistic Regression-----------------------------------------------
#    t1 = time.time()
#    clf = linear_model.LogisticRegression()
#    elapsed = time.time() - t1
#    print('ML model computation time :: %.10f\n' % (elapsed))
##    ML 3 : Adaboost Classifier-----------------------------------------------
#    clf = AdaBoostClassifier(n_estimators=2)
##    ML 4 : Linear SVC -------------------------------------------------------
#    t1 = time.time()
    clf = svm.LinearSVC(penalty='l2', loss='hinge', dual=True, tol=0.0001, C=1.0)
#    elapsed = time.time() - t1
#    print('ML model computation time :: %.10f\n' % (elapsed))
#    
    
    
    fit = clf.fit(train_x,train_y)
    if i == 0:
        y_score = fit.decision_function(test_x)
    cv = cross_val_score(clf, data[data_features[0:9]], data["routeoption"], cv=10)
#    np.append
    test_pred = clf.predict(test_x)
    cvmean = cvmean + cv.mean()
    cvstd = cvstd + cv.std()
    accuracy = accuracy + accuracy_score(test_y, test_pred, normalize = True)
#    print("why?")

cvmean = cvmean/10
cvstd = cvstd/10
accuracy = accuracy/10
#print("Target Day of the week: %s" %dayofweek)
print("Model Accuracy: %0.3f" %accuracy)
print("Accuracy(Mean CV): %0.3f (+/- %0.3f)" % (cvmean, cvstd * 2))


fpr = dict()
tpr = dict()
roc_auc = dict()
test_y_array= test_y.as_matrix(columns=None)

fpr, tpr, threshold = roc_curve(test_y_array, y_score, pos_label=1)
roc_auc = auc(fpr, tpr)
plt.figure()
lw = 2
plt.plot(fpr, tpr, color='green',
         lw=lw, label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC curve for Adaboost')
plt.legend(loc="lower right")
plt.show()
#
#count1 = 0
#count2 = 0
#for index, row in data.iterrows():
#    if row["routeoption"] == 1:
#        count1 = count1 +1
#    else:
#        count2 = count2 +1
#        
#print(count1)
#print(count2)
#for ys in y_score:
#    fpr = dict()
#    tpr = dict()
#    roc_auc = dict()
#    for i in range(2):
#        fpr[i], tpr[i], _ = roc_curve(test_y[:, i], ys[:, i])
#        roc_auc[i] = auc(fpr[i], tpr[i])
##        plt.figure()
#        lw = 2
#        plt.plot(fpr[2], tpr[2], color='darkorange',
#                 lw=lw, label='ROC curve (area = %0.2f)' % roc_auc[2])
#        plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
#        plt.xlim([0.0, 1.0])
#        plt.ylim([0.0, 1.05])
#        plt.xlabel('False Positive Rate')
#        plt.ylabel('True Positive Rate')
#        plt.title('Receiver operating characteristic example')
#        plt.legend(loc="lower right")
#        plt.show()
#plt.plot(range(0,100), cvs, 'bo')
#plt.show()


#Useful Split method that renders 10-fold cross validation.

#def split(data_pca):
#    data_pca = data_pca.reindex(np.random.permutation(data_pca.index))
#    data_pca.to_csv("/Users/dohoonkim/Desktop/cse517a/ApplicationProject/shuffled.csv",index=False)
#    data_pca = pd.read_csv("/Users/dohoonkim/Desktop/cse517a/ApplicationProject/shuffled.csv")
#    for i in range(0,10):
#        """for last test set, we grab 159 data points"""
#        if i==9:
#            testdata = data_pca[160*i:1599]
#            excluded = list(range(160*i,1599))
#            bad_df = data_pca.index.isin(excluded)
#            newdata = data_pca[~bad_df]
#            traindata = newdata
#            testdata.to_csv("/Users/dohoonkim/Desktop/cse517a/ApplicationProject/test%d.csv"%i,index=False)
#            traindata.to_csv("/Users/dohoonkim/Desktop/cse517a/ApplicationProject/train%d.csv"%i,index=False)
#        else: #0~8 for other cases, 160 data points
#            testdata = data_pca[160*i:(i+1)*160]
#            excluded = list(range(160*i,(i+1)*160))
#            bad_df = data_pca.index.isin(excluded)
#            newdata = data_pca[~bad_df]
#            traindata = newdata        
#            testdata.to_csv("/Users/dohoonkim/Desktop/cse517a/ApplicationProject/test%d.csv"%i,index=False)
#            traindata.to_csv("/Users/dohoonkim/Desktop/cse517a/ApplicationProject/train%d.csv"%i,index=False)
