'''EXCEPTION HANDLING'''
##
##There are 2 stages where error may happen in a program
##1) During compoilation > syntax error
##2) During Execution > exeptions
##
##'''SYNTAX ERROR:'''
##    something in the program is not written according to the program grammar
##    Error is raised by the interpreter/compiler
##    you can solve it by rectifying the program
##
##Examples of syntax error
##
##print 'hello world'
##
##1) leaving symbols like :,(),;....
##2) misspelling of a keyword
##3) incorrect indentation'
##4) empty if/else/loops/class/functions
##
##
##a = 5
##if a == 3
##print('hi')
##
##a = 5
##iff a == 3
##print('hi')
##
##'''IndexError'''
##the IndexError is thrown when trying to access an item at an invalid index.
##L = [1,2,3]
##print(L[100])
##
##
##
##'''ModuleNotFoundError'''
##the ModuleNotFoundError is thrown when a module is not found
##import mathi
##math.floor(5.3)
##
##
##'''KeyError'''
##the KeyError is thrown when a key is not found
##d = {'name':'nitish'}
##d['age']
##
##
##'''TypeError'''
##the ypeError is thrown when an operation or function is applied to an object of an inappropriate type
##1+'a'
##
##'''ValueError'''
##the ValueError is thrown when a function's argument is of an inappropriate type
##int('a')
##
##'''NameError'''
##the NameError is thrown when an object could not be found
##print(k)
##
##'''AttributeError'''
##L = [1,2,3]
##L.upper()


'''

'''

####Let's create a file
##with open('sample.txt','r') as f:
##    f.write('hello world')
##
##
####try catch demo
##
##try:
##    with open('sample.txt','r') as f:
##        print(f.read())
##except:
##    print('sorry file not found')


'''catching specific exception'''    

##f = open('sample.txt','x')  #creates file
## 
##try:
##    m = 14
##    f = open('sample.txt','r')
##    print(f.read())
##    print(m)
##except FileNotFoundError:
##    print('file not found')
##except NameError:
##    print('variable not defined')
##    


'''Generic Exception'''

####Generic except statement should always be at the last,
####since python executes line-by-line


##f = open('sample.txt','x')  #creates file
##f = open('sample.txt','w')  #write mode
##f.write('L = [1,2,3,4]')
##f.close()
##try:
##    m = 14
##    f = open('sample.txt','r')
##    print(f.read())
##    print(m)
##    print(5/2)
####    print(5/0)
##    L = [1,2,3,4]
##    L[100]
##except FileNotFoundError:
##    print('file not found')
##except NameError:
##    print('variable not defined')
##except ZeroDivisionError:
##    print('number cannot be divided by 0')
##except Exception as e:
##    print(e.with_traceback)
    
'''-------------------------------------------'''


##fi = open('new.txt','x')
##
##fi = open('new.txt','w')
##fi.write('hello new')
##
##fi.close()
##try:
##    m = 14
##    fi = open('new.txt','r')
##    print(fi.read())
##    
##    print(m)
##
##    print(5/2)
####    print(5/0)
##    L = [1,2,3,4]
##    L[100]
##    
##except FileNotFoundError:
##    print('file not found')
##except NameError:
##    print('variable not defined')
##except ZeroDivisionError:
##    print('number cannot be divided by 0')
##except Exception as e:
##    print(e.with_traceback)


'''else and finally'''

##try:
##    f = open('sample.txt','r')
##    n = 1
##    print(n)
##    print(o)
##except FileNotFoundError:
##    print('file not found')
##except NameError:
##    print('tujhe define krna bhul gaye')
##except Exception:
##    print('kuch toh hai')
##else:
##    print(f.read())
##finally:
##    print('kuch bhi ho...mujhko print hona hai')
##
####it follows diamond approach    


'''
raise exception


in python programming, exceptions are raised when errors occur in runtime
we can also manually raise exceptions using the rasie keyword.
we can optionally pass values to the exception to clarify why that exception was raised

'''
##
##class Bank:
##    def __init__(self,balance):
##        self.balance = balance
##
##
##    def withdraw(self,amount):
##        if amount < 0:
##            raise Exception('amount cannot be negative')
##        if self.balance < amount:
##            raise Exception('paise nahi hai tere paas')
##        self.balance -= amount
##
##obj = Bank(10000)
##
##try:
##    obj.withdraw(-5000)
##except Exception as e:
##    print(e)
##else:
##    print(obj.balance)




##class SecurityError(Exception):
##  def __init__(self,message):
##    print(message)
##
##  def logout(self):
##    print("logout")
##
##class Google:
##  def __init__(self,name,email,password,device):
##    self.name=name
##    self.email=email
##    self.password=password
##    self.device=device
##
##  def login(self,email,password,device):
##    if device != self.device:
##      raise SecurityError("you gone")
##    if email == self.email and password == self.password:
##      print("welcome")
##    else:
##      print("login Error")
##    
##obj = Google('bhumika','bhumika@123.com','1234','Android')     
##
##try:
##  obj.login("bhumika@123.com",'1234','Windows')
##except SecurityError as e:
##  e.logout()
##else:
##  print(obj.name)
##finally:
##  print("database connection close")


