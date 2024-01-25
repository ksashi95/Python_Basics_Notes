# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 15:05:31 2024

@author: ashik
"""
import pandas as pd

df1 = pd.read_excel(r"C:\Users\ashik\Downloads\Sample - Superstore.xlsx")
df1


import matplotlib.pyplot as plt


top5 = df1.sort_values("Profit",ascending = False)
top5 = top5.head(5)


plt.scatter(top5.Category,top5.Profit)
plt.scatter(top5.Category,top5.Quantity)
plt.scatter(top5.Category,top5.City)
# ----------------------------
import seaborn as sns

sns.countplot(data = df1,x = "Category",hue = "Segment")

sns.scatterplot(data = df1,x = "Category",y ="Profit",hue = "Segment")

sns.barplot(data = df1,x = "Category",y ="Profit",hue = "Segment")

sns.lineplot(data = df1,x = "Category",y ="Profit",hue = "Segment")

sns.histplot(data = df1,x= "Category",y ="Profit")

sns.boxplot(data = df1,x = "Category",y ="Quantity",hue = "Segment")

sns.stripplot(data = df1,x = "Category",y ="Quantity",hue = "Segment")



