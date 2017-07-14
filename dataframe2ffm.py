# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 21:13:04 2017

@author: Administrator
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from pandas import get_dummies
import gc

def pandas_onehot(df, col):
    df = get_dummies(df, columns=col)
    return df

def sklearn_onehoot(df):
    enc = OneHotEncoder()
    enc.fit(df.drop(['label'], axis=1))  
    data = enc.transform(df.drop(['label'], axis=1)).toarray()
    return data

def data_convert2ffm(df, ffmfile): 
    columns = df.columns.values
    d = len(columns)
    feature_index = [i for i in range(d)]  #默认从0开始
    field_index = [0]*d #初始化参数
    field = [] #初始化参数
    for col in columns:
        field.append(col.split('_')[0])  #onehot选出编码前的变量
    index = -1
    for i in range(d):
        if i==0 or field[i]!=field[i-1]:  #判断是否在同一个field里面
            index += 1
        field_index[i] = index           #默认从0开始

    with open(ffmfile, 'w') as f:
        for row in df.values:
            line = str(row[0])  #label
            for i in range(1, len(row)):
                if row[i]!=0:
                    line += ' ' + "%d:%d:%d" % (field_index[i], feature_index[i], row[i]) + ' '
            line += '\n'
            f.write(line)
    
    print('finishing......')
  
    
    
    
    
