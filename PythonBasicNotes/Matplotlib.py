# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 15:02:30 2024

@author: ashik
"""
# -----------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt


a = [1,2,3,4]
b = ["ash","may","taral","geet"]



plt.bar(b,a)   #barchart
plt.show()

plt.plot(b,a)   #linechart
plt.show()
plt.plot(b,a,marker ="*",color = "red",mec = "green",linestyle ="dotted")   #line graph
plt.grid(color = "pink",linestyle ="dotted")
plt.show()
plt.scatter(b,a,color = "blue")   #scatter plot
plt.show()


# -------------------------------------------------------------------

a = [11,22,33,44,55]
b = ["A","B","C","D","E"]

# linechart
plt.plot(b,a,linestyle = "dashdot",marker = "o" ,mec = "black",mfc = "yellow", color = "red")
plt.grid(linestyle = "dashed",color = "grey")
plt.xlabel("variables")
plt.ylabel("marks")
plt.title("details of grade")

# ---------------------------------------------------------------------

# barchart
plt.bar(b,a,linestyle = "dashdot",color = "red")
plt.grid(color = "grey")
plt.xlabel("variables")
plt.ylabel("marks")
plt.title("details of grade")


# ---------------------------------------------------------------------

# horizontal barchart
plt.barh(b,a,color = "red")
plt.grid(linestyle = "dashed",color = "grey")
plt.xlabel("variables")
plt.ylabel("marks")
plt.title("details of grade")


# ---------------------------------------------------------------------

# scatter
plt.scatter(b,a,linestyle = "dashdot",marker= "s",s = 505 ,color = "red")
plt.grid(linestyle = "dashdot",color = "grey")
plt.xlabel("variables")
plt.ylabel("marks")
plt.title("details of grade")


# ---------------------------------------------------------------------

# Histogram
"categorical data"
a = ["python","SQL","Excel","SQL","SQL","SQL","python","python","Excel","power BI"]

plt.hist(a,linestyle = "dashdot",color = "red")
plt.grid(linestyle = "dotted",color = "grey")
plt.xlabel("variables")
plt.ylabel("marks")
plt.title("details of grade")


# ------------------------------------------------------------------
"with  numerical data"
a = [11,22,11,33,44,11,55]

plt.hist(a,linestyle = "dashdot",color = "red",bins = [0,25,50,75])
plt.grid(linestyle = "dashed",color = "grey")
plt.xlabel("variables")
plt.ylabel("marks")
plt.title("details of grade")



# ----------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt

a = [11,22,33,44]
b = ["A","B","C","D"]


plt.subplot(1,2,1)

plt.pie(a,labels = b,explode = [0,0,0.2,0],autopct = "%1.0f%%")
plt.legend()



plt.subplot(1,2,2)

plt.scatter(b,a)
plt.title("scatter plot")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.grid()




plt.subplot(1,2,1)

plt.pie(a,labels = b,explode = [0,0,0.2,0],autopct = "%1.0f%%")
plt.legend()



plt.subplot(1,2,2)

plt.scatter(b,a)
plt.title("scatter plot")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.grid()

# ------------------------------------
plt.subplot(2,2,1)

plt.pie(a,labels = b,explode = [0,0,0.2,0],autopct = "%1.0f%%")
plt.legend()



plt.subplot(2,2,2)

plt.scatter(b,a)
plt.title("scatter plot")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.grid()


plt.subplot(2,2,3)

plt.pie(a,labels = b,explode = [0,0,0.2,0],autopct = "%1.0f%%")
plt.legend()


# -----------------------------------------------------------------
plt.subplot(2,2,1)

plt.pie(a,labels = b,explode = [0,0,0.2,0],autopct = "%1.0f%%")
plt.legend()



plt.subplot(2,2,2)

plt.scatter(b,a)
plt.title("scatter plot")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.grid()



plt.subplot(2,2,3)

plt.scatter(b,a)
plt.title("scatter plot")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.grid()


plt.subplot(2,2,4)

plt.pie(a,labels = b,explode = [0,0,0.2,0],autopct = "%1.0f%%")
plt.legend()

# -------------------------------------------------

plt.subplot(2,1,2)

plt.scatter(b,a)
plt.title("scatter plot")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.grid()


plt.subplot(2,1,1)

plt.pie(a,labels = b,explode = [0,0,0.2,0],autopct = "%1.0f%%")
plt.legend()


# plt.figure(figsize=(10,4))

