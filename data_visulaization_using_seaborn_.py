# -*- coding: utf-8 -*-
"""Data Visulaization using seaborn .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1q5yWTOiI5I07EXXIhp4H68KnebrmQ634
"""

import numpy as np
import pandas as pd

import seaborn as sns

df = pd.read_csv('/content/breast-cancer.csv')

#EDA

df.head(10)

df.tail(10)

df.shape

df.info()

df.describe()

#Data Visulaization using basic seaborn types
   #It is similar to matplotlib.pyplot and sns has advanced data storage and types

a=df['area_mean']
b=df['id']
sns.lineplot(x=a,y=b,data=df)

c=df['compactness_mean']
d=df['compactness_worst']
sns.scatterplot(x=c,y=d,data=df)

e=df['area_worst']
f=df['compactness_worst']
sns.barplot(x=e,y=f,data=df)

sns.countplot(x='area_worst',data=df)

sns.pairplot(df,hue='area_worst')