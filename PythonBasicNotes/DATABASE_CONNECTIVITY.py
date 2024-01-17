##'''DATABASE CONNECTIVITY'''

##import pymysql
##from pymysql import *
####import pymysql.cursors
##
##
##
##username = input('enter your name: ')
##password = input('enter your password: ')
##
##
##c = connect(host = 'localhost',user = 'root',password = 'root',database = 'ninja')
##e = c.cursor()
##e.execute("insert into logged values('{}','{}');".format(username,password))
##e.execute('select * from logged;')
####e.execute("delete from logged where username = 'jijhh';")
##print(e)
##
##for i in e:
##    print(i)
##
##c.commit()  #save data in database
##c.close()   #close connection
##
##
'''THREADING'''
##threads are a way to achieve concurrent execution of code.
##Threads allow you to run multiple tasks concurrently, making
##better use of available CPU cores and improving the overall
##performance of your application. Python provides a built-in
##module called threading to work with threads.
##
##Thread: A thread is the smallest unit of a process. Multiple threads can run within a single process.

##class Hello (Thread) :
##    def run (self) :
##        for i in range (50) :
##            print ("mayuri")
####            sleep(1)
##
##
##            
##class Hi (Thread) :
##    def run (self) :
##        for i in range (50) :
##            print ("Hi")
####            sleep(1)
##t1 = Hello ()
##t2 = Hi ()
####t1.run ()
####t2.run ()
##
##            
##t1.start ()
##sleep(0.2) ##unsynchro
##t2.start ()
####
######main thread
##t1.join()
##t2.join()
####
####
##print("i am here")

