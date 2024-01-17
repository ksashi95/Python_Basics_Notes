##'''MODULE
##
##1. Module are nothing but group of functions,variables & class that are saved in a file.
##2. Modules and Packages are used when you don't want to share your entire code
##   with the client and show only the required data.
##3. Code Reusability Syntax: import module_name
##
##
##Types of Module
##
##1)Pre-defined - random,calendar,keyword
##
##ex:
##1st.py
##def show():
##    print('hello')
##
##
##
##2)User-defined
##
##ex:
##2nd.py
##import 1st
##1st show()
##
##
##'''
##
##import calendar
##print(calendar.month(2023,12))
##
##
##import keyword
##print(keyword.kwlist)
##
##help('calendar')


###packages
##In Python, a package is a way of organizing related modules into a single directory hierarchy.
##This allows you to create a modular and organized structure for your code.
##this is use for big projects(more mosdule to manage)
##its provide us ability to have only one import statement to access all the
##functionality from all the module
##

##import my_package.my_module

##from . import module_name  # Import module_name from the same package
##from .. import another_package  # Import a package from the parent directory

##import my_package.module1
##import my_package.subpackage.submodule1
##ex:-
##import game.level.start
##game.level.start.select_difficulty(2)

##since the proess is len.. so insited of  this we can go on * function

##from math import*
##from math import pi
##print("the value of pi is", pi)
##x=min(35,10,25)
##x=max(5,10,25)
##x=abs(-7.34)
##x=pow(4,3)
##print(x)

##import math
##x = math.sqrt(64)
##x = math.ceil(1.4)##up to nearest integer
##x = math.floor(1.4)##down to nearest integer
##print(x)

##import datetime
##x=datetime.datetime.now()##show current date and time
####1st name of the module
####2nd  This is a class within the datetime module. 
##print(x)
##print(x.year)##give year
##print(x.strftime("%C"))##day's of week
##print(x.strftime("%B"))##month


