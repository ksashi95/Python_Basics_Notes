# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

emp = {'emp1':['ankit','mumbai',20000],'emp2':['anas','pune',21000],'emp3':['fiaz','kolhapur',22000],'emp4':['sameer','nagpur',23000],'emp5':['suyash','navi mumbai',24000]}

print(emp)

# ------------------------------------------------------

# to download libraries
#pip install pandas

import pandas as pd
#pandas is used for data analysis,
#data cleaning,
#data sorting,
#graphs

a = {"emp_name":["Mayuri S","Mayuri R","K S Ashish","ankit","anas","Mithilesh"],
     "emp_id":[1,2,3,4,5,6],
     "desg":["PM","AM","TL","PM",'AM','AM']
     }

df1 = pd.DataFrame(a)

print(df1)
df1
df1.info()

# objects = string

# --------------------------------------------------------

#to fetch column(s)

# Method 1

#df["columnName"]    --> to fetch single column

df1["emp_name"]
df1["emp_id"]
df1["desg"]


#df[["columnName"]]   --> to fetch multiple columns
df1[["emp_name","emp_id","desg"]]



# method 2

#df.columnName

df1.emp_name
df1.emp_id

# df1.emp name (will not work when column name has a space in between)

# --------------------------------------------------------------
# INDEXING

# iloc & loc
# iloc = index location

# df.iloc[row number,column number]


df1.iloc[3,:]
df1.iloc[1,:]
df1.iloc[0:2,:]

df1.iloc[0:2,1:3]
df1.iloc[1:3,0:2]


# -------------------------
# loc = location

# df1.loc[row number,column name]

df1.loc[0:2,:]
df1.loc[0:2,["emp_name","emp_id"]]

# df1.loc[0:2,1:]  #won't work



# task
# df1

# df1.iloc[0:3:2,:]

# df1.loc[0:4:3,["emp_name", "emp_id", "desg"]]



df1.iloc[[0,3],:]

df1.loc[[0,3],:]

df1.iloc[[0,3],0]

df1.iloc[[0,3],0:2]

b = 7.7
c = 1


# data types in pandas int64,object,dataframe,datetime64[ns],float64

# ---------------------------------------------
# TO FIND UNIQUE VALUES
df1.desg.unique()
df1['desg'].unique()


# TO FIND THE COUNT OF UNIQUE VALUES
df1.desg.nunique()

a = {"emp_name":["Mayuri S","Mayuri R","K S Ashish","ankit","anas","Mithilesh","Mithilesh"],
     "emp_id":[1,2,3,4,5,6,6],
     "desg":["PM","AM","TL","PM",'AM','AM',"AM"]
     }

df2.desg.unique()  
df2.desg.nunique() #count of unique values


df2 = pd.DataFrame(a)

df1.duplicated()

df2.duplicated()

df2.desg.duplicated()

# --------------------------------------
df2.duplicated().sum()

df2.desg.duplicated().sum()

# ----------------------------------------

df1

# methods of saving a dataframe to different file formats
df1.to_excel(r"C:\Users\ashik\AppData\Local\Programs\Python\Python312\dummy.xlsx") #regex

df1.to_csv(r"C:\Users\ashik\AppData\Local\Programs\Python\Python312\dummy1.csv")

df1.to_csv(r"C:\\Users\\ashik\\AppData\\Local\\Programs\\Python\\Python312\\dummy1.csv")


# ----------------------
#method to read

df1 = pd.read_excel(r"C:\Users\ashik\Downloads\Sample - Superstore.xlsx")

df1.info()
# df1.City


# -------------------------------

# save 3 method
df1.to_html(r"C:\\Users\\ashik\\AppData\\Local\\Programs\\Python\\Python312\\dummy3.html")

df1.to_json(r"C:\Users\ashik\AppData\Local\Programs\Python\Python312\dummy4.json",orient = "records")



# read 4 method
df1 = pd.read_csv(r"C:\Users\ashik\AppData\Local\Programs\Python\Python312\dummy1.csv")

df1 = pd.read_html(r"C:\Users\ashik\AppData\Local\Programs\Python\Python312\dummy3.html")




# zomato ---> rest_name, dish type,phone , city  reviews and ratings
# rows  - 11
# unique

z = {"rest_name":["The Earth Plate","Namak","Fiona","Ummrao",
                       "Tanatan","Rasoi Kitchen & Bar","Tanatan",
                       "Saptami","Jyran-Tandoor Dining & Lounge",
                       "Solitiare Restaurant","Lake View Cafe"],
     
          "dish_type":["Dessert Indian","Indian","Italian",
                       "Indian","Bar","Asian","Indian",
                       "Indian","International","Indian",
                       "Indian Cafe"],
          
          "phone":[8792829230,879780982,9928983298,327276872,
                   2830870202,387208732,2983908232,976979808,
                   9980982687,587780982,2388092331],
          
          "location":["Vile Parle East","Colaba","Powai","Juhu",
                      "Borivali","Juhu","Colaba","Bhandup",
                      "Goregaon East","Khandivali","Borivali"],
          
          "reviews":["delicious","tasty","mouth-watering","appetizing",
                     "tasty","delicious","satisfying","delightful",
                     "enjoyable","mouth-watering","appetizing"],
          
          "ratings":[4.3,4,5,4.2,4.5,3,4,5,4.3,4.1,4]
          }


df5 = pd.DataFrame(z)


import pandas as pd


df5.to_excel(r"C:\Users\ashik\AppData\Local\Programs\Python\Python312\rest_df.xlsx")

df5.to_csv(r"C:\Users\ashik\AppData\Local\Programs\Python\Python312\rest1_df.csv")

df6 = pd.read_excel(r"C:\Users\ashik\Downloads\Sample - Superstore.xlsx",sheet_name='People')


# TO READ SQL DATA
import pymysql


c = pymysql.connect(host = 'localhost',user = 'root',password = 'root',database = 'world') 
#connecting to mysql database

df7 = pd.read_sql('show tables;',con = c)
#query to show tables

df7 = pd.read_sql('select * from city;',con = c)
#query to select all data from the table

# -------------------------------------------------------------------------------

ab = {"emp_name":["Mayuri S","Mayuri R","K S Ashish","ankit","anas","Mithilesh"],
     "emp_id":["a","b","c","d","e","f"],
     "desg":["PM","AM","TL","PM",'AM','AM']
     }

df1 = pd.DataFrame(ab,index=["a","b","c","d","e","f"]) #index change

print(df1)
df1
df1.info()


df1.loc[["a","c"],:]

df1.loc[["a"]]

df1.iloc[0,1:4]

df1.sort_values("desg",ascending=True)

# ---------------------------------------------------------------------------
df1.desg.unique()

df1.desg.nunique()

import numpy as np #to find missing values

abc = {"emp_name":[np.nan,"Mayuri R","K S Ashish",np.nan,"anas","Mithilesh"],
     "emp_id":[1,2,3,4,np.nan,6],
     "desg":["PM",np.nan,"TL","PM",'AM','AM']
     }

df1 = pd.DataFrame(abc)

df1

# -------------------------------
sorting


df1.sort_values("desg",ascending=True) 

df1.sort_values("desg",ascending=False)  #descending order



df1.sort_values("emp_name",ascending=True)

df1.sort_values(["emp_name","desg"],ascending=[True,False])


# ----------------------------------------------------
# missing value functions

df1.isnull()
df1.isnull().sum()

df1.isna()
df1.isna().sum()

df1.notnull()
df1.notnull().sum()

df1.notna()
df1.notna().sum()

# -----------------------------------------------------

df1.iloc[2,1] = 33 #permanently replaces both exisiting and blank values 
df1
df1.fillna("ABC")  #temporarily changed

df1.emp_id.fillna(33,inplace = True) # for permanent change
df1

# --------------------------------------------------------

import pandas as pd
import numpy as np

df1

#drops rows with blank values
df1.dropna() 

# df.dropna(inplace = True) #drops blank values permamnently
df1.dropna(inplace = True) 
df1

# df.drop(columns=["column1","column2","column3"],inplace = False) #drops columns
df1.drop(columns= ["desg"]) 

df1

#REARRANGING COLUMNS
df1.iloc[:,[1,0,2]]

df1 = df1[["desg","emp_name","emp_id"]]

df1

#RENAMING COLUMN NAMES
# df.rename(columns = {"old_name":"new_name"},inplace = False)
df1.rename(columns={"emp_name":"empname"})

# ----------------------------------------------------------


mail = pd.read_excel(r"C:\Users\ashik\Downloads\Sample - Superstore.xlsx")
mail

mail.info()
mail.drop(columns = ["Order Date","Ship Date"],inplace = True)
mail

mail.groupby("Category").min()
mail.groupby("Category").max()
mail.groupby("Category").count()
mail.groupby("Category").mean()
mail.groupby("Category").sum()
mail.groupby(["Category","Region"]).sum()

mail.sort_values(["Region","Category"],ascending = [True,False])

# ------------------------------------------------------------

import pandas as pd


a = {
     "emp_name":["Mayuri S","Mayuri R","K S Ashish","Mithilesh"],
     "emp_id":[1,2,3,4],
     "desg":["PM","AM","TL","PM"]
     }

df1 = pd.DataFrame(a)
df1

b = {
     "emp_id":[1,5,7,4,6],
     "salary":[111,222,333,444,555]
     }

df2 = pd.DataFrame(b)
df2

# MERGE

df1.merge(df2,how="left")
df1.merge(df2,how="right")
df1.merge(df2,how="outer")
df1.merge(df2,how="inner")


# CONCAT

pd.concat([df1,df2],axis= "rows")

pd.concat([df1,df2],axis= "columns")



df1 = pd.read_excel(r"C:\Users\ashik\Downloads\Sample - Superstore.xlsx")

df1.sample(20) #random data

df1.head()  #by default top 5 rows
df1.head(10) #top 10 rows

df1.tail()   #by default bottom 5 rows
df1.tail(10)   #bottom 10 rows

print(df1.to_string())

# for numerical data
df1.nlargest(5,"Profit")  
df1.nsmallest(5,"Profit")

# to fetch specific columns
df1[["Profit","Quantity","Region"]].nlargest(5,"Profit")
df1[["Profit","Quantity","Region"]].nsmallest(5,"Profit")


# pd.set_option('display.max_columns',21)

# pd.set_option('display.max_rows',10)








# ---------------------------------------------------------

