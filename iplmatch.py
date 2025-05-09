# -*- coding: utf-8 -*-
"""iplmatch.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17N1wbxBfzB2GIBEtUHsSgelKQR3XGhV2
"""

cd /content/drive/My Drive/ipl-match-predictor

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv(r'D:\new project titils and documentation pdf\Game Difficulty Balancing Using Player Behavior Prediction\ipl-match-master\cleaned.csv')
data

data.to_csv(r'D:\new project titils and documentation pdf\Game Difficulty Balancing Using Player Behavior Prediction\ipl-match-master\cleaned.csv',index=False)

features=data.iloc[:,[2,4,5,6,7]]
labels=data.iloc[:,10]
data['city'].unique()

s=data[data['city']==18]
s

a=s[s['winner']==9]
a['city'].replace(18,4,inplace=True)
a

data=data.append(a,ignore_index=True)

data.drop(data[data['city']==3].index,inplace=True)

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import sklearn.metrics as m
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,train_size=0.9,random_state=71)
model4=RandomForestClassifier(n_estimators=100,max_depth=25,random_state=129)
model4.fit(features_train,labels_train)
label_predict_4=model4.predict(features_test)
m.accuracy_score(labels_test,label_predict_4)

import pickle
w

pickle.dump(model4,open("model.pkl",'wb'))

model=pickle.load(open('model.pkl','rb'))

label_predict=model.predict(features_test)
m.accuracy_score(labels_test,label_predict)

