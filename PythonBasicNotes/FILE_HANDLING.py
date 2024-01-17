'''FILE HANDLING'''


'''
Why we save data in file?
FILE: they are name of location on disk to store related information

they are used to store data permanently in non-volatile memory(ex: hard drive)

WHY?
RAM is a volatile memory so we use file for storing data PERMANENTLY


OPERATION IN FILE:

Methods --> open(),read,readlines(),write(),writelines(),close()
Mode --> r(read),w(write),a(append),x(create),r+(read and write),w+,
         a+,regex--r(Regular Expression)
'''
##f = open('./demo.txt','r')   #open('file path','mode')


##open mode

##f1 = open('file_1.txt','x')   #creates
##f1  is a pointer


##read mode
'''
it is by default opening mode of file
it will give error (input/output) when file is not present
file handler is present at the eginning of the file
'''

f1 = open('file_1.txt','r')   
##data = f1.read()    #reading file content
##print(data)


##write mode
'''
this will open the file in write mode only we cannot read it.
it overwrites the content of the file or it will create new file
file pointer is at the beginning
'''
##f2 = open('file_2.txt','w')
##
##f1 = open('file_1.txt','w')
##f1.write('how are you?')
##f1.close()


##f1 = open('file_1.txt','r')
##print(f1.read())
##f1.close()

##read and write mode
'''
open the file in both read and write mode
if file not exist it will give error
file pointer is at the beginning
'''


##f1 = open('file_3.txt','r+')
##f1 = open('file_1.txt','r+') #it will not erase the content of the file
##print(f1.tell()) #tells the position of the pointer
##
##f1.write('hi')
##print(f1.tell())
##
##print(f1.read())
##print(f1.tell())
##
##f1.write('thanks for lecture')
##print(f1.read())
##f1.close()

'''23.11.2023'''
##write and read mode
'''
file pointer is at the beginning
it overwrites the content of the file or it will create a new file
here, first write then read
'''

##f1 = open('file_1','w+')
##print(f1.tell())
##
##f1.write('courses 1,2,3,4,5,6')
##print(f1.tell())
##f1.seek(0)   #seek method moves cursor
##
##data = f1.read()
##print(data)
##print(f1.tell())
##
##f1.write('hello')
##print(f1.tell())
####f1.seek(3)
##data =(f1.read())
##print(data)
##f1.close()

##Append mode
'''
open file in write mode
file pointer is at the end of the file
it adds new content to the file or creates a new file
data will be added at the end of the file
'''

##f1 = open('file_1.txt','a')
##f1.write('hi')
##f1.write('\n hello')
##f1.write('\n how are you?')
##
##f1.close()


##f1 = open('file_1.txt','r')
##print(f1.read())
##
##f1.close()

##Append+ mode
'''
will open the file in read and write mode
file pointer is at the end of the file
it adds the content to the file or creates a new file
'''

##f1 = open('file_1.txt','a+')
##print(f1.tell())
##
##f1.write('hello students')
##print(f1.tell())
##
####f1.seek(0)
####print(f1.tell())
##
##print(f1.read())
##print(f1.tell())
##
##f1.write('come in')
##print(f1.tell())
##f1.seek(0)
##
##print(f1.tell())
##print(f1.read())
##
##f1.close()
