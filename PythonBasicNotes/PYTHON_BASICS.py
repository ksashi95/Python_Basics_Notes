##PYTHON BASICS
##
####class 1
##
##
##print("hello python i am here")
##
##a =45
##b = 500
##print("the difference of number is :",b-a)
##
##
##help("keywords")
##
##help("for")
##
##help("try")
##
##some@name = "abc"
##print(some@name)
##
##
##
##some2name = "abcd"
##print(some2name)
##
####-----------------------------------------------------

## python class2
##'''valid varibales'''
##
##my_var
##var2
##count_
##
##
##'''invalid varibale names'''
##
##1count
##my name = "aks"
##roll-no = 76
##
##x,y,z = "orange","banan","cherry"
##x,y,z = "orange",14,"cherry"
##print(x)
##print(y)
##print(z)
##
##x=y=z ="sepal" #assigning single value to multiple varibales
##
##
##fruit = ['a','b','c']
##x,y,z = fruit    # x,y,z = ['a','b','c']
##print(x)
##print(y)
##print(z)
##print(fruit)
##
##
##different data types stored in some variables
##
##
##
##
##
##'''implicit type conversion/ data lose'''
##
##int_num =5
##float_num= 3.14
##result = int_num+float_num
##print(result)
##
##bool_val = True
##result = bool_val+5
##print(result)
##
##c= "ram"
##n = 3
##print(c*n)
##
##
##bool_value =False
##str_val = "string"
##add = bool_value+str_val
##print(add)
##
##mystr = "pen"
##myfloat = 2.5
##myadd = mystr+myfloat
##print(myadd)
##
##'''explicit type conversion(type casting)'''
##
##a = 32
##a1 =  str(a)  
##print(type(a1))
##
##
##
##a2 = bool(a)
##print(type(a2))
##
##
##short way
##sen = float(565)
##print(sen)
##print(type(sen),'side is float type data =',sen)
##
##string = float("python")
##print(string)
##print(type(string))
##
##string = float("34")
##print(string)
##print(type(string))
##
##tuple_data = (1,2,3)
##print(type(str(tuple_data)))
##
##'''i/o user function'''
##variable = input([prompt])
##
##place = input('state or city: ')
##name = input('enter your name: ')
##age = int(input('enter your age: '))
##print(name,age)
##print('your name is',name,'and your age:',age)
##print(type(name))
##
##
##x = "sonali"
##print(x)
##print( "name = \n",x)  # \n - new line
##
##
##name = input("enter your name: ")
##age = int(input("enter your age: "))
##contact_no = int(input(" enter your phone number: "))
##print("my name is",name,",i am",age,"years old and my contact number is:",contact_no)
##
##
##stud_name = str(input("Enter your Name: "))
##stud_age = int(input("Enter your age: "))
##stud_city = str(input("Enter your city: "))
####stud_phone = int(input("Enter your phone: "))
##print("My name is ",stud_name,"\nI am ",stud_age," years old","\nI am from ",stud_city)
##
##python class3
##
##'''OPERATORS
##ARITHMETIC OPERATORS'''
##
##n1 = 10
##n2 = 3
##n = n1-n2
##print(n)
##
##print(n1+n2)
##
##str1 = "hello"
##str2 = "india"
##print(str1+str2)
##print(str1+" "+str2)
##
##str1 = "hello"
##n1 = 14.0
##print(str1+n1)
##
##print('addition is ',5+6)
##
##num1 = 30
##num2 = 10
####print(num1/num2) #quotient
##
##print(num1//num2)  #floor division
##
##num3 = 26
##num4 = 5
##print(num3%num4) #remainder
##
##print(3**3) #exponent
##
##
##
##'''ASSIGNMENT OPERATORS'''
##
##num1 =2
##num2 = num1
##print(num2)
##
##num3 = 10
##num4 = 2
##num3 += num4 # num3+num4
##print(num3)
##
##num5 = 3
##num6 = 4
##num5 *= num6
##print(num5)
##
##num7 = 8
##num8 = 3
##num8 -= num7
##print(num8)
##num7 -= num8
##print(num7)
##
##'''COMPARISON OPERATORS(== , != , >= , <=)'''
##
##num1 = 10
##num2 = 2
##
##print(num1 == num2)
##print(num1 != num2)
##print(num1 >= num2)
##print(num1 <= num2)
##
##
##'''LOGICAL OPERATORS (and, or , not)'''
##
##num1 = 10
##num2 = -20
##
##print(num1 == 10 and num2 == -20)
##print(num1 == 10 or num2 == -20)
##print(num1 != 10 or num2 == -20)
##print(not(num1 == 10))
##
##'''MEMBERSHIP OPERATORS:IN,NOT IN'''
##
##numSeq = [1,2,3]
##
##print(2 in numSeq)
##print(5 in numSeq)
##print(2 not in numSeq)
##print(5 not in numSeq)
##
##task- 23/3 - 5 * 7(14-2) //precedence of operators
##num - 20.4
##3.0 + 3.14
##
##print((23/3) - 5 * (7*(14-2)))
##
##'''LOGICAL STATEMENT/ DECISION MAKING STATEMENT/ CONTROL FLOW STATEMENT'''
##
##''' syntax: if(condition):
##                          statement/ifbody
##            else:
##                 else body
##'''
##
## if statement
##x= 1
##
##if x >5:
##  print("x is greater than 5")
##
## if-else statement
##
##a = 33
##b = 303
##a = int(input("enter a number a: "))
##b = int(input("enter a number b: "))
##
##if a > b:
##    print("a is greater than b")
##else:
##    print("a is less than b")
##
##
##
##age =  int(input("enter your age: "))
##if age >= 18:
##    print("you are legal to drive")
##else:
##    print("you are below 18")
##
##
##'''EVEN ODD PROGRAM'''
##
##a = int(input("enter a number: "))
##if a % 2 == 0:
##    print("a is even")
##else:
##    print("a is odd")
##
##
##
##task- check divisibility
##num1 = int(input("enter a number:"))
##
##if num1%2 == 0 and num1%3 == 0:
##    print("number is divisdible by both 2 and 3")
##else:
##    print("number is not divisible by 2 and 3")
##
##
##
##'''check for vowel (case-sensitive)'''
##
##letter = str(input(" enter a letter: "))
##if letter in ["a","e","i","o","u","A","E","I","O","U"]:
##    print("is a vowel")
##else:
##    print("not a vowel")
##
##
##'''program to check whether a number entered is three digit number or not?'''
##num5 = int(input("enter a number:"))
##if num5 >=100 and num5 <1000:
##    print("number is a 3 digit number")
##else:
##    print("is not a 3 digit number")
##
##        #OR
##        
##num = int(input("enter a number:"))
##str_num = str(num)
##length = len(str_num)
##
##if len(str_num) == 3:
##    print("is a 3 digit number")
##    mid_digit = int(str_num[1])
##    print('middle digit is',mid_digit)
##
##else:
##    print("is not a 3 digit number")
##
##
##
##'''IF ELIF ELSE'''
##
##a = int(input("enter a number: "))
##if a%2 == 0:
##    print(" is divisible by 2")
##elif a%5 ==0:    
##    print(" is divisible by 5")
##else:    
##    print(" is notdivisible by 2 or 5")
##
##
##
##temp =  float(input("enter a nuimber: "))
##if temp <= 22:
##    print("temperature is low")
##elif temp >22 and temp <45:
##    print("temperature is high")
##else:
##    print(" temperature is too high")
##
##
##
##
##'''CALCULATOR'''
##num6 = int(input("enter a number: "))
##num7 = int(input("enter a number: "))
##op= input("enter an operator (+,-,*,/): ")
##if  op == "+":
##    print(num6+num7)
##elif op == "-":
##    print(num6-num7)
##elif op == "*":
##    print(num6*num7)
##elif op == "/":
##    print(num6/num7)
##else:
##    print("end")
##
##
##
##'''NESTED IF-ELSE STATEMENT'''
##
##a = int(input("enter a number: "))
##if a%2 == 0:
##    print("number is divisible by 2")
##    if a%5 == 0:
##        print("number is divisible by 5")
##    else:
##        print("number is not divisible by 5")
##else:
##    print("number is not divisible by 2")
##
##
##
##age = int(input("enter a number: "))
##if age >= 18:
##    print("you are an adult")
##else:
##    if age >=13 and age <18:
##        print("you are a teenager")
##    else:
##        print("you are a child")
##        
##
##
##short_hand if-else
##
##
##
##'''pass //used to write empty loop
##// used to write to avoid error'''
##
##a = 33
##b = 44
##if b>a:
##    pass
##
##
##
##a= 10
##if a > 5:
##    print("a is greater than 5")
##else:
##    pass #(no action taken)
##
##
##code continues here
##print("code continues...")
##
##
##usernum1 = int(input("enter a number: "))
##if usernum1 > 0:
##    print(usernum1,"number is a positive number")
##    print("...")
##elif usernum1 == 0:
##    print("the number you entered is",usernum1)    
##else:
##print(usernum1,"number is a negative number")
##
##
##'''LOOP - executes a block of code repeatedly'''
##'''syntax: for values in collection of set:
##          for body receives output in iteration sequence'''
##
##
##
##loops - for loop(finite)
##        while loop(infinte)
##
##
##for data in dataset
##
##data = ['siddharth','soham','omkar','python',"98",9898]
##for x in data:
##    print('the names are-',x)
##print(x)
##
##
##
##for a in 'python':
##    print(a)
##
##    
##for loop
##'''syntax: range(start,end,step) last element excluded
##
##for (variablename) in range(stopvalue)'''
##
##for x in range(5):  #n-1 concept
##    print(x)
##
##for x in range(5,50):
##    print(x)
##
##for c in range(21,0,-1):
##    print("current number is ", c)
##
##
##for c in range(2,15,2):
##    print("current number is ", c)
##
##
##for z in range(-11,3):
##    print("current number is ", z)
##
##
##for items in range(5): #outer loop with items ranging from 0-5
##    for values in range(items): #inner loop with values ranging from 0 to 'items -1'
##        print("*",end="a")# print the value of values on the same line as the asterisk
####        print(values)
##    print() #print a new line after each inner loop completes
##
##for items in range(5,0,-1): #outer loop with items ranging from 0-5
##    for values in range(items): #inner loop with values ranging from 0 to 'items -1'
##        print("*",end=" ")# print the value of values on the same line as the asterisk
####        print(values)
##    print() #print a new line after each inner loop completes
##    
##
##'''JUMPING STATEMENT: break, continue, pass(error handling)'''
##
##for x in range(1,10):
##    pass
##print(x)
##
##
##
##fruits = ["apple","banana","kiwi","cherry"]
##for x in fruits:
##    if x == "banana":
##        continue
##    print(x)
##else:
##    print("else block")
##
##
##fruits = ["apple","banana","kiwi","cherry"]
##for x in fruits:
##    if x == "banana":
##        break
##    print(x)
##            
##
##m = ["live",'for','tech','andheri']
##for x in m:
##    print("check values",x)
##    if 'tech' in x:
##        print('tech is there')
##        break
##
##
##
##m = ["live",'for','tech','andheri']
##for x in m:
##    print("check values",x)
##    if 'tech' in x:
##        print('tech is there')
##        continue
##
##
##'''WHILE LOOP'''
##
##'''SYNTAX: while condition:
##                (body)'''
##
##while True:
##    print("LiveTechIndia")
##
##
##while 1:
##    print("python here")
##    break
##
##i = 0
##while i>0:
##    print(i)
##    i+=1
##
##
##i = 5
##while i>0:
##    print(i)
##    i+=1
##
##
##
##while True:
##    age = int(input(" enter your age: "))
##    print(age+5)
##
##
##'''PROGRAM TO PRINT A TABLE'''
##
##while 1:
##    number = int(input(" enter a number to print table: "))
##    for x in range(1,11):
##        result = number * x
##        print(number,"X",x,"=",result)
##
##    print("Do you want to continue?")
##    check = input("Type YES or NO: ").lower()
##
###no1 = "NO"
###no2 = 'no'    
##
##    if check ==  'no': #no1 or check == no2
##        print("Thankyou for visiting our site")
##        break
##    elif check != 'no' or check != 'yes':
##        print("....")
##        break
##    else:
##        continue
##
##    
##stud_name = ['faiz','ankit','ashish','anas']
##
##for x in stud_name:
##    if x == "ashish":
##        break
##    elif x == "anas":
##        continue
##    print(x)   
##
##
##
##stud_name = ['faiz','ankit','ashish','anas']
##
##for x in stud_name:
##    if 'ashish' in x:
##        print(x)
##        break
##    elif 'anas' in x:
##        print(x)
##        continue
##    print(x)   
##
##
##       
##'''NESTED WHILE'''
##
##
##a = 0
##while a<= 10:
##    #   a+=1
##      print("python",a)
##      a+=1 #a = a+1
##while True:
##    number = int(input("enter any positive number to continue /start:"))
##    if number < 0:
##        print("you have stop the code")
##        break
##    else:
##        print("you have entered: ",number)
##    
##'''WHILE LOOP: with the while loop we can execute a set
##of statements as long as a condition is true
##
##CONTINUE STATEMENT: with continue statement we can stop
##the current iteration, and continue with the next:
##
##'''
##
##
##
##
##i = 0
##while i <6:
##      #i+=1
##    if i ==3:
##        pass
##        continue
##    i+=1
##    print(i)
##
##
##
##
##a = 0b11 #binary - start with 0b
##print(a)
##
##d= 10 #decimal - regular numbers
##print(d)
##
##b = 0o13 #octadecimal - start with 0o
##print(b)
##
##c = 0x13 #hexadecimal - start with 0x
##print(c)
##
##
##
##f= 2e2 #e = 10 float literals
##print(f)
##
##g =1.5*100 #e2 =100
##print(g)
##
##w = 0+3.14j ##a+ib complex literals
## print(w)
##
##multi_string = """"multi line string"""
##print(multi_string)
##uni_code = u"\U0001f923\U0001F606\U0001f600"
##print(uni_code)
##
##a = True+4
##b = False+4
##print(a,"A")
##print(b,"B")
##
##
##'''SPECIAL LITERAL: none'''
##
##a = None
##print(a)
##
##
##
##
##
##import random
##
##jackpot = random.randint(1,100)
##guess = int(input("enter your number: "))
##counter = 1
##
##while guess != jackpot:
##    if guess < jackpot:
##        print("guess higher")
##    else:
##        print("guess lower")
##
##    guess = int(input("guess"))
##    counter +=1
##
##
##print("your guess is correct")
##print("you took",counter,"attempts")
##                  
##
##
##user1 = "Asus123"
##passw = "123456"
##
##for i in range(4):
##
##    username = str(input("please enter your username: "))
##    password = str(input("please enter your password: "))
##
##    if username == user1 and password == passw:
##        print("login successful")
##        break
##    else:
##        print("please try again")
##        continue
##
##
##
##
##user1 = "Asus123"
##passw = "123456"
##
##
##for i in range(5):
##    if i<=3:
##        username = str(input("please enter your username: "))
##        password = str(input("please enter your password: "))
##        if username == user1 and password == passw:
##            print("login successful")
##            break
##        else:
##            print("please try again")
##    else:
##         print("something went wrong")
##      
##
##
##user1 = "Asus123"
##passw = "123456"
##
##
##for i in range(5):
##    if i<=3:
##        username = str(input("please enter your username: "))
##        if username == user1:
##            password = str(input("please enter your password: "))
##            if password == passw:
##                print("login successful")
##                break
##            else:
##                print("please try again")
##        else:
##         print("something went wrong")
##
##
##'''
##DATA TYPES are of 4 types: NUMBER, SEQUENCE, SETS, MAP
##
##NUMBER: int, float, complex
##SEQUENCE: str, list, tuple
##SETS: set
##MAP: dic
##'''
##
##
##
##'''
##DATA STRUCTURES: #in-built(Predefined) & user-defined
##
##Data Structures are used to manage data i.e., add,append,delete,
##access,insert.
##
##A String is a  "Sequence of characters"
##A String is  a sequence of Unicode characters
##'''
##
##Creating Strings
##Accessing Strings
##Adding Characters to Strings
##Editing Strings
##Deleting Strings
##Operations on Strings
##String Functions
##
##
##'''Creating Strings'''
##
##c= 'hello'
##print(c)
##
##c='''hello'''
##print(c)
##
##c="""hello"""
##print(c)
##
##c = str("hello")
##print(c)
##print(type(c))
##
##'''Accessing Strings''' ##INDEXING (used only to extract single elements)
##
##c = "Hello_World!"
##print(c[0])
##print(c[-1])
##print(c[4])
##print(c[-5])
##
##Type of indexing -ve and +ve
##
##'''Slicing''' ##used to extract multiple elements
##Syntax: variable_name[start,end,step]
##
##print(c[0:4])
##print(c[2:])
##print(c[:4])
##print(c[:])
##print(c[2:6:2])
##print(c[0:6:-1])
##print(c[-5:-1:2])
##print(c[::-1])
##print(c[-1:-5:-1])
##print(c[-5:-1])
##print(c[-1:-5])
##
##
##D = "abcdefghij"
##print(D[2:7:2])
##
##D = "abcdefghij"
##print(D[0:6:-1])
##
##'''Editing & Deleting in String'''
##
##Editing
##c[0] = "X"
##strings are IMMUTABLE data type
##
##c = "world" ##here we are doing reassignment
##print(c)
##
##c = 15
##print(c)
##
##
##'''Deleting'''
##del c
##print(c)
##
##
##c = "hello"
##del c[0]
##
##
##del c[:3:2]
##
##
##
##'''OPERATIONS ON STRINGS
##
##ARITHMATIC OPERATIONS
##'''
##
##a ="Hello"+" "+"World" #concatenate
##print(a)
##
##
##print("*"*10) #multiplication
##
##b = "hello"-"hello" #subtraction
##print(b)
##
##c = "a"/"a" #division
##print(c)
##
##
##String data type performs only 2 arithmatic operations
##i.e., Addition & Multiplication
##
##
##'''RELATIONAL OPERATIONS'''
##
##print("Hello"  == "hello")
##
##print("hello" != "world")
##
##print("Mumbai" > "Pune")
##
##print("Kolkata" > "Goa")
##
##print("kolkata" > "Goa")
##
##print("Mumbai" > "Mumbaj")
##
##
##
##'''
##LOGICAL OPERATION
##
##AND OPERATOR
##
##'''
##
##print("hello" and "Hello")
##
##print("" and "")
##
##print("Hello" and "World")
##
##print("Hello" and "")
##
##print("Hello" and "hello")
##
##print("" and "Hello")
##
##print("Hello" and "Hello")
##
##print("World" and "Hello")
##
##print("Hello" and "world")
##
##print("" and "2")
##print("" and "")
##print("1" and "")
##print("1" and "2")
##print("2" and "1")
##
##'''
##
##In Python, the [and] operator returns the first false operand or the last operand if both are true.
##If both operands are non-empty strings, they are considered truthy values.
##In this case, the [and] operator returns the second operand.
##
##In summary,when both operands are non-empty strings, the [and] operator returns the second operand
##'''
##
##'''
##OR OPERATOR
##'''
##
##print("" or "2")
##print("" or "")
##print("1" or "")
##print("1" or "2")
##print("2" or "1")
##
##
##'''
##NOT OPERATOR
##'''
##
##print(not "hello")
##
##print(not"")
##
##print(not" ")
##
##
##'''
##LOOPS OPERATOR
##'''
##
##c = "Hello World!"
##
##for i in c:
##    print(i)
##
##for i in c[2:7]:
##    print(i)
##
##for i in c[2:7:2]:
##    print(i)
##
##for i in c[::-1]:
##    print(i)
##
##for i in c[-6:-2]:
##    print(i)
##
##for i in c[-8:-2:2]:
##    print(i)
##
##for i in c[-2:-6:-2]:
##    print(i)
##
##for i in c[-2:-6]:
##    print(i)
##
##
##'''
##MEMBERSHIP OPERATOR
##'''
##c = "Hello World!"
##
##print("H" in c)
##
##print("h" in c)
##
##print("hlo" in c)
##
##print("h","l","o" in c)
##
##print("h" not in c)
##
##
##'''
##STRING METHODS (Built_in functions)
##'''
##
##
##'''len(): Returns the length of an object '''
##print(len(c))
##
##'''max(): Returns the largest of an object [depends on ASCII values]'''
##print(max(c))
##
##'''min(): Returns the smallest item in an iterable'''
##print(min(c))
##
##'''sorted(): Returns a sorted list[gives output in ascending order]
##   empty values < special characters < Uppercase < lowercase
##
##   Note: You cannot sort a list that contains BOTH
##   string values AND numeric values.
##'''
##
##print(sorted(c))
##
##print(sorted(c,reverse=True))
##
##a = (1, 11, 2)
##x = sorted(a)
##print(x)
##
##a = ("h", "b", "a", "c", "f", "d", "e", "g")
##x = sorted(a)
##print(x)
##
##a = ("h", "b", "a", "c", "f", "d", "e", "g")
##x = sorted(a, reverse=True)
##print(x)
##
##a = ("H", "b", "a", "C", "f", "d", "h", "g")
##x = sorted(a, reverse=True)
##print(x)
##
##
##
##
##
##'''To call a function: variable_name. and press Tab key
##'''
##
##c = "iT iS RainING OutSIdE"
##
##'''capitalize(): Converts the first character to upper case
##'''
##print(c.capitalize())
##
##
##'''title(): Converts the first character of each word to upper case
##'''
##print(c.title())
##
##
##'''upper(): Converts a string into upper case
##'''
##print(c.upper())
##
##
##'''lower(): Converts a string into lower case
##'''
##print(c.lower())
##
##
##'''swapcase(): Swaps cases, lower case becomes upper case and vice versa
##'''
##print(c.swapcase())
##
##
##'''count(): Returns the number of times a specified value occurs in a string
##'''
##print(c.count("a"))
##print(c.count("m"))
##print(c.count("r")) #case-sensitive
##print(c.count("he"))
##
##
##'''find(): Searches the string for a specified value and
##           returns the position of where it was found
##'''
##c = "iT iS RainING OutSIdE"
##
##print(c.find("RainING"))
##print(c.find("ainING"))
##print(c.find("R"))
##print(c.find("he"))
##
##'''NOTE: Returns the lowest index of the substring if found.
##         Returns -1 if the substring is not found.
##         Does not raise an exception..
##'''         
##
##
##'''index(): Searches the string for a specified value and
##            returns the position of where it was found
##'''
##c = "iT iS RainING OutSIdE"
##
##print(c.index("a"))
##print(c.index("RainING"))
##print(c.index("ainING"))
##print(c.index("R"))
##print(c.index("he"))
##
##'''NOTE: Returns the lowest index of the substring if found.
##         Raises a ValueError if the substring is not found.
##'''         
##
##'''
##endswith(): Returns true if the string ends with the specified value
##'''
##print(c.endswith("ING"))
##print(c.endswith("dE"))
##print(c.startswith("dE"))
##print(c.startswith("iT"))
##
##
##'''
##FORMATTING
##'''
##
##print("Hello my name is {} and I am {}".format("Python",30))
##
##print("Hello my name is {0} and I am {1}".format("Python",30))
##
##print("Hello my name is {name} and I am {age}".format(name="Python",age=30))
##
##name = "Python"
##age = 30
##
##'''f is used at the beginning of a string for formatting'''
##
##format_string = f"Hello my name is {name} and I am {age}" 
##print(format_string)
##
##
##'''
##use to Ask Questions
##'''
##
##
##'''isalnum(): alphabetic/numeric/ alphanumeric '''
##print("FLAT20".isalnum())
##print("fiat".isalnum())
##print("20".isalnum())
##print("abc20@!".isalnum())
##
##
##'''isalpha()'''
##print("FLAT20".isalpha())
##print("fiat".isalpha())
##print("20".isalpha())
##print("abc20@!".isalpha())
##
##
##
##'''isdigit()'''
##print("FLAT20".isdigit())
##print("fiat".isdigit())
##print("20".isdigit())
##print("abc20@!".isdigit())
##
##
##'''isidentifier(): Returns True if the string is an identifier'''
##
##print("FLAT20".isidentifier())
##print("fiat".isidentifier())
##print("20".isidentifier())
##print("abc20@!".isidentifier())
##print("abc_".isidentifier())
##
##
##'''split(): You use it when you want to break a string into a
##   list of substrings based on a specified delimiter.
##'''
##
##sentence = "Hello, how are you today?"
##words = sentence.split()  # Defaults to splitting on spaces
##print(words)
##
##
##csv_data = "apple,orange,banana,grape"
##fruits = csv_data.split(',')
##print(fruits)
##
##
##'''join(): instead of breaking a string into a list,
##   it joins the elements of an iterable (like a list) into a single string.'''
##
##fruits = ['apple', 'orange', 'banana', 'grape']
##csv_data = ','.join(fruits)
##print(csv_data)
##
##word_list = ['Hello', 'world', 'how', 'are', 'you']
##sentence = ' '.join(word_list)
##print(sentence)
##
##
##'''replace(): It allows you to replace a specified
##   substring with another substring.'''
##
##original_string = "I like programming in Python."
##new_string = original_string.replace("Python", "JavaScript")
##print(new_string)
##
##
##'''You can also specify an optional third argument to
##   limit the number of replacements
##'''
##
##original_string = "I like Python, Python is fun, Python is powerful."
##new_string = original_string.replace("Python", "JavaScript", 2)
##print(new_string)
##
##
##original_string = "I like Python, Python is fun, Python is powerful."
##new_string = original_string.replace("Python", "JavaScript", 3)
##print(new_string)
##
##
##
##'''strip(): removes leading and trailing whitespaces
##   (including spaces, tabs, and newline characters) from a string.
##   It doesn't affect the spaces within the string,
##   only those at the beginning and end.
##'''
##
##text = "   This is a text with extra spaces.   "
##stripped_text = text.strip()
##print(stripped_text)
##
##'''lstrip(): removes only leading spaces.
##   rstrip(): remove only trailing spaces.
##'''
##
##text = "   This is a text with extra spaces.   "
##left_stripped_text = text.lstrip()
##right_stripped_text = text.rstrip()
##
##print(left_stripped_text)
##print(right_stripped_text)
##
##
##
##'''
##LIST
##'''
##
##
##'''creating List'''
##
##L = [] #empty list
##print(L)
##
##L=[23,345,3445]
##print(L)
##
##
##numbers=[1,2,3,4,5,6,7]
##print(numbers)
##print(type(numbers))
##
##'''HETEROGENOUS LIST'''
##
##p = [1,2,3.4,"ABC","abc",True,2+3j]
##print(p)
##
##'''MULTI-DIMENSIONAL LIST/NESTED LIST'''
##
##r = [2,23,2434,[3,4,5],3]
##print(r)
##
##r = [2,23,2434,[3,4,5],[23,344],3]
##print(r)
##
##s = [[2,3],[4,5],[6,7]]
##print(s)
##
##'''from_list_constructor'''
##
##L = list("hello")
##
##L2 = list("Haldia")
##print(L2)
##
##t5 = list(["one",])
##print(t5)
##
##
##L3 = list("H","a","l") #error
##print(L3)
##
##
##'''ACCESSING LIST'''
##
##L = [23,345,56]
##print(L[-1])
##
##l3 = [1,2,3,[4,5]]
##print(l3[-1])
##
##x = l3[-1]
##print(x)
##
##print(x[0]) #x=l3[-1]
##
##l4 = l3[-1][0]
##print(l4)
##
##print(l3[-1][-1])
##
##l4 = [[[1,2],[3,4]],[[5,6],[7,8]]]
##
##print(l4[-1])
##
##print(l4[0][-1][-1])
##
##print(l4[0][1][1])
##
##print(l4[-2][-1][-1])
##
##print(l4[1][0][0])
##
##print(l4[-1][-2][-2])
##
##print(l4[-1][0][0])
##
##
##'''
##EDIT ITEM
##'''
##
##l = [1,2,3,4,5]
##print(l)
##print(id(l))
##
##l[0] = 100 # 1 is replaced by 100
##print(l)
##print(id(l))
##
##l[-1] = 500 # 5 is replaced by 500
##print(l)
##print(id(l))
##
##l[2] = "a"
##print(l)
##
##
##'''
##SLICING
##'''
##
##l1 = l[1:4]
##print(l1)
##
##l3 = [1,2,3,[4,5],6] #MULTI-DIMENSIONAL SLICING
##l1 = l3[1:4][-1][-2]
##print(l1)
##
##l1 = l3[1:4][3][0]
##print(l1)
##
##
##
##'''
##APPEND: Adding new items to the List
##'''
##l = [1,2,3,4]
##
##l.append(1000)
##print(l)
##
##l.append([5,6])
##print(l)
##
##
##l.append("abc")
##print(l)
##print(id(l))
##
##l.append(500,455,344) #error
##print(l)
##
##l.append([500,455,344])
##print(l)
##
##
##'''
##EXTEND: also used to add new items to the list
##'''
##l = [1,2,3,4]
##
##l.extend([500,455,344])
##print(l)
##
##l.extend([20,"a"])
##print(l)
##
##
##'''
##INSERT
##
##syntax: varname.insert(index,value)
##
##'''
##l = [1,2,3,4]
##
##l.insert(1,"world")
##print(l)
##
##l.insert(0,6)
##print(l)
##
##'''
##del
##'''
##
##
##l = [1,2,3,0]
##del l
##print(l)
##
##
##l2 = [1,2,3,4,5,"hi"]
##del l2[-3:]
##print(l2)
##
##
##del l2[-3:-1]
##print(l2)
##
##'''
##.remove : when we dont know the position
##'''
##
##l1 = [1,2,3,4,5,"hi","abc",3]
##l1.remove("hi")
##print(l1)
##
##
##'''
##.pop :  deletes the last item in a list
##'''
##
##l1.pop()
##print(l1)
##
##
##'''
##.clear : it will give empty list
##'''
##
##l1.clear()
##print(l1)
##
##
##
##operations in list
##
##l1=[2,35,7,4,3,1]
##l2=[3,6,4,63]
##
##print(l1+l2)
##print(l1*3)
##
##l3=[3,55,5,6,7,[3,4]]
##
##for x in l3:
##    print(x)
##
##print(4 in l3)
##print([3,4] in l3)
##
##print(l1)
##print(len(l1))
##print(max(l1))
##print(min(l1))
##
##
##sorting in python done by two methods sort,sorted means it will give data in ascending and descending order
##
##print(sorted(l1))                      ##sorted will not make changes in same list
##print(sorted(l1,reverse=True))
##
##print(l1.sort())                         ##sort will make changes in same list
##print(l1)
##
##
##print(l1.index(3))
##print(l1.index(4))
##
##
##
##print("hello how are you?".title())
##
##sample = "hello how are you?"
####String concatenating
##L =[]
##print(sample.split())
##for i in sample.split():
##    print(i)
##    print(i.capitalize())
##    L.append(i.capitalize())
##print(L)
##print(" ".join(L))
##
##
##
##'''
##LIST COMPREHENSION : List particular into a new List
##'''
##
##w = ["fan","keys","chair","AC","armed"]
##newlist = []
##for x in w:
##    if "e" in x:
##        newlist.append(x) #adding elements into newlist
##print(newlist)        
##
##
##l1 = [1,2,3,4,5]
####print(l1)
##l2 = []
##for i in l1:
##    l2.append(i**2)
##print(l2)
##
##[or]
##
##l1 = [1,2,3,4,5]
####print(l1)
##l2 = []
##for i in l1:
##    x = i**2
##    l2.append(x)
##print(l2)
##
##
##'''
##TUPLE: defined within (), allows duplicate data, nested tuple,can have multiple data type,
##single element is separated by (,), immutable
##'''
##
##g = (1,2,3,4,5,5)
##print(g)
##print(type(g))
##
##r = (1,2.0,"abc",("python",True,20),34,34)
##print(r)
##print(type(r))
##
##'''
##Accesing data
##'''
##
##print(g[4])
##print(g[-5])
##print(r[3][0:2])
##
##
##'''
##Replacing
##'''
##
##g[4] = 6767  
##print(g)
##print(id(g))
##
##'''
##len()
##'''
##
##g = (1,2,3,4,5,5)
##r = (1,2.0,"abc",("python",True,20),34,34)
##
##print(len(g))
##t = g+r  #concatenation
##print(t)
##print(len(t))
##
##'''
##Data change in Tuple
##
##
##tuple()--> List[]-->tuple()
##'''
##
##
##x = ("apple","cherry","banana","mango","orange")
##print(x)
##print(id(x))
##
##y = list(x)
##print(y)
##print(id(y))
##
##y[1] = "watermelon"
##print(y)
##print(id(y))
##
##x = tuple(y)
##print(x)
##print(id(x))
##
##
##
##
##'''
##Concatenation of Tuples
##'''
##
##t = (56,33,45,22,(4,5,6,889),344)
##t1 = (55,66,77,88)
##t+=t1 ## t = t+t1
##
##print(t)
##
##'''
##INDEXING
##'''
##x = g.index(4)
##print(x)
##'''-----------------------------'''
##'''TUPLE'''
##
##'''Creating tuple'''
##
##T = ()
##print(T)
##print(type(T))
##
##
##'''Muti-Dimensional Tuple'''
##T = (1,2,3,4,"a")
##print(T)
##print(type(T))
##
##
##'''
##TUPLE CONSTRUCTOR - tuple()
##
##NOTE: When creating a tuple with only one item,
##remember to include a comma after the item,
##otherwise it will not be identified as a tuple.
##
##'''
##
##t2 = tuple((1,)) #takes only one argument
##print(t2)
##
##
##t3 = tuple(("one",))
##print(t3)
##
##t4 = tuple(("one"))
##print(t4)
##
##t5 = list(["one",])
##print(t5)
##
##
##'''Accessing tuple elements'''
##
##t =(1,2,3,5,"a",3.0,True)
##print(t[0])
##print(t[6])
##print(t[-2])
##
##t6 = (((1,2),(3,4)),((5,6)))
##print(t6)
###access 3
##print(t6[0][1][0])
###access 5
##print(t6[-1][0])
##
##
##'''
##Once a tuple is created, you cannot change its values.
##Tuples are unchangeable, or immutable as it also is called.
##
##But there is a workaround. You can convert the tuple into a list,
##change the list, and convert the list back into a tuple.
##'''
##
##'''Edit Item: Tuple is IMMUTABLE'''
##
##t =(1,2,3,5,"a",3.0,True)
##print(t)
##print(id(t))
##
####t[0] = 10 
####print(t) #error
##
####'''Slicing'''
##
##t =(1,2,3,5,"a",3.0,True)
##print(t[1:4])
##
##
##t6 = (((1,2),(3,4)),((5,6),(7,8)))
##print(t6[0])
##print(t6[1])
##print(t6[1:2])
##print(t6[1:2][0])
##
##'''APPEND not possible since tuple is immutable'''
##
##t =(1,2,3,5,"a",3.0,True)
##print(t)
##
##l = list(t)
##print(l)
##
##l.append(1000) #adds new element at the end of the list
##print(l)
##
##t = tuple(l)
##print(t)
##
##l1 = list(t)
##print(l1)
##
##l1.extend([50,45])
##print(l1)
##
##t1 = tuple(l1)
##print(t1)
##
##
##'''
##Insert
##'''
##
##t =(1,2,3,5,"a",3.0,True)
##print(t)
##
##
##'''syntax: varname.insert(index,value)'''
##
##l2 = list(t)
##l2.insert(1,3+4j)
##
##t3 = tuple(l2)
##print(t3)
##
##
##'''
##del: Tuples are unchangeable,
##so you cannot remove items from it,
##but you can use the same workaround
##as we used for changing and adding tuple items
##
##'''
##
##t7 = (2,5,"a",5.0,"hello")
##print(t7)
##del t7
##print(t7)
##
##
##t7 = (2,5,"a",5.0,"hello")
##print(t7)
##
##print(len(t7))  #tuple length
##
##
##del t7[1:3]
##print(t7)
##
##del t7
##print(t7)
##
##
##'''
##Add/Join tuple to a tuple
##'''
##t8 = (2,3,4,"b")
##t9 = ("abc",4.0,False)
##tadd = t8+t9
##print(tadd)
##
##'''
##Multiply Tuples
##'''
##
##t8 = (2,3,4,"b")
##mtuple = t8*2
##print(mtuple)
##
##
##
##
##
##'''
##Packing a tuple:
##'''
##
##fruits = ("apple", "banana", "cherry")
##print(fruits)
##
##
##'''
##Unpacking a tuple: extract the values back into variables.
##'''
##
##fruits = ("apple", "banana", "cherry")
##
##(green, yellow, red) = fruits
##
##print(green)
##print(yellow)
##print(red)
##
##
##'''
##NOTE: The number of variables must match the number of values in the tuple,
##      if not, you must use an asterisk to collect the remaining values as a list.
##'''
##
##
##'''
##Using Asterisk*
##---------------
##If the number of variables is less than the number of values,
##you can add an * to the variable name and the values will be
##assigned to the variable as a list
##'''
##
##fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
##
##(green, yellow, *red) = fruits
##
##print(green)
##print(yellow)
##print(red)
##
##
##'''
##If the asterisk is added to another variable name than the last,
##Python will assign values to the variable until the number of
##values left matches the number of variables left.
##'''
##
##fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
##
##(green, *tropic, red) = fruits
##
##print(green)
##print(tropic)
##print(red)
##
##
##'''
##LOOP TUPLES
##'''
##
##fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
##for i in fruits:
##     print(i)
##
##'''
##Loop Through the Index Numbers
##'''
##
##fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
##for i in range(len(fruits)):
##     print(i)
##
##
##
##fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
##for i in range(len(fruits)):
##     print(fruits[i])
##
##
##
##fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
##for i in fruits:
##    if "apple" in fruits:
##        pass
##print("exists")
##
##
##'''
##Using a While Loop
##'''
##
##fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
##i = 0
##while i < len(fruits):
##    print(fruits[i])
##    i = i+1
##
##
##
##'''
##Tuple Methods
##'''
##
##'''count(): Returns the number of times a specified value occurs in a tuple
##    SYNTAX: tuple.count(value)
##'''
##
##t10 = (1,3,454,"name","234",True,454,True,234)
##print(t10.count(454))
##
##print(t10.count(234))
##
##
##
##'''index(): Searches the tuple for a specified value and returns
##            the position of where it was found
##            
##            The index() method raises an exception if the value is not found.
##
##'''
##
##t10 = (1,3,454,"name","234",True,454,True,234)
##print(t10.index(234))
##print(t10.index("234"))
##
##print(t10.index(2))
##
##
##'''----------------------------'''
##
##'''
##DICTIONARY: defined within {key:Value},elements separated by(,),mutable,
##Doesn't not allow duplicate KEYS,can have multiple values
##'''
##
##d = {1:'java',2:'python',3:'R',4:'C++'}
##print(d)
##print(type(d))
##
##
##d1 = {"model":"honda","fruit":"apple","language":["java","python","R"],2:4}
##print(d1)
##
##d2 = {
##      2:4,
##      "complex":2+3j,
##      'veh':{"vehicle":["car","bus"],2:12},
##      "gender":["M","F"]
##     }
##print(d2)
##
##
##
##nested_dict = {
##               "key1":"value1",
##               "key2":{"key21":"value21","key22":"value22"},
##               "key3":"value3"
##              }
##print(nested_dict)
##
##
##'''
##ACCESSING DATA in Dictionary
##'''
##
##d = {1:'java',2:'python',3:'R',4:'C++'}
##print(d[2])
##
##d1 = {"model":"honda","fruit":"apple","language":["java","python","R"],2:4}
##print(d1["model"])
##
##d = {1:'java',1:3,2:'python',3:'R',4:'C++'} #Duplicacy is not allowed
##print(d)
##
##
##
##
##d = {'k1':[1,2,3,{'ormg':[1,2,3,{"nested_list":[4,5,6,7,"Hello"]}]}]}
##print(d['k1'])
##print(d['k1'][3]['ormg'][3]['nested_list'][4])
##
##
##'''---------------------------------------------------'''
##
##'''REPLACE DATA'''
##
##
##
##
##
##'''DICTIONARY METHODS'''
##
##f = {"model":"honda","year":2022,"colour":["red","blue","green"]}
##print(f)
##
##
##'''ACCESSING DATA'''
##
##print(f.keys())
##
##print(f.values())
##
##print(f.items()) #results in the form of tuples
##
##print(f.get("model"))  #database connectivity
##
##print(f["model"])   #dict_name[key_name]
##
##y = f.get('year')
##print(y)
##
##'''REMOVING DATA'''
##
##f = {"model":"honda","year":2022,"colour":["red","blue","green"]}
##f.pop("model")
##print(f)
##
##
##f = {"model":"honda","year":2022,"colour":["red","blue","green"]}
##f.popitem()  #by default removes the last item in the dictionary 
##print(f)
##
##f = {"model":"honda","year":2022,"colour":["red","blue","green"],1:3}
##f.popitem()
##print(f)
##
##
##f = {"model":"honda","year":2022,"colour":["red","blue","green"]}
##del f["year"]
##print(f)
##
##del f
##print(f) #NameError
##
##'''UPDATE DICTIONARY'''
##
##f = {"model":"honda","year":2022,"colour":["red","blue","green"]}
##print(f)
##
##
##f.update({"fruits":["apple","banana","oranges"],"mileage":"125kmph"})
##print(f)
##
##
##'''LOOPS IN DICTIONARY'''
##
##f = {"model":"honda","year":2022,"colour":["red","blue","green"]}
##
##for x in f.keys():
##    print(x)
##print(len(f))    
##
##
##f = {"model":"honda","year":2022,"colour":["red","blue","green"]}
##
##print(f.copy) #creates a copy of the dictionary
##print(id(f))
##
##g = dict(f)
##print(g)
##print(id(g))
##
##
##print(f.clear()) # clears entire dictionary resulting in empty dictionary
##
##f = {"model":"honda","year":2022,"colour":["red","blue","green"]}
####print(f)
##print(f.fromkeys("z","honda"))
##
##z= {}
##print(z.fromkeys("z","honda"))
##print(f.fromkeys("year"))
##
##f = {"model":"honda","year":2022,"colour":["red","blue","green"]}
##d = dict(p="42",q="*")
##
##print(d.fromkeys(d,f))
##
##
##
##
##f = {"model":"honda","year":2022,"colour":["red","blue","green"],2:"35"}
##print(f)
##
##print(f.setdefault(2,45))   
##print(f)
##
##print(f.setdefault(3,"book"))
##print(f)
##
##
##
##'''
##SETS : defined within {}, separated by comma, no duplicacy,
##       immutable, unordered, multiple data types
##'''
##
##
##s = {1,2,3,4,5,4,4,45,66,3,2,5}
##print(s)
##print(id(s))
##print(type(s))
##
##t = {1,2,3,4,5,("a",4,4,5,3),2,45}
##print(t)
##
##n = {"a",1,2.5,True,2,bool}
##print(n)
##
##b = {}
##print(b)
##print(type(b)) #dict
##
##
##a={True,"a",2,3.3,bool}
##print(a)
####
##sw = set()
##print(sw)      #typeCAST
##print(type(sw))
##
##
##_set = {()}       
##print(type(_set))
##
##
##set1 = {""}
##print(type(set1))
####
####
##a = {1,2,3,4,4,5,5,5,6}
##print(a)
##
##b = {"abc","xz",(789),0}
##print(b)
##
##a.add(74)
##print(a)
##
##a.update(b)
##print(a)
##
##
##b.update(a)
##print(b)
##
##a.discard(5)
##print(a)
##
##b.remove('abc')
##print(b)
##
##'''SET doesn't allow mutable data types.
##   SET itself is a mutable data type.
##'''
##
##set2 = {1,2,3,4,5,["a",4,4,5,3],2,45}  #set doesn't allow mutable data type & list is a mutable datatype
##print(set2)
##
##set3 = {1,2,3,4,5,{"key":"value"},2,45} #set doesn't allow mutable data type & dict is a mutable datatype
##print(set3)
##
##set4 = {{1},{2}}  #set itself is a mutable datatype
##print(set4)
##
##
##'''
##ACCESSING ITEMS is NOT POSSIBLE
##'''
##s = {1,2,3,4,4,5,5,5,6} #Error
##print(s[2])
##
##s[2] = 100  #Error
##print(s)
##
##
##
##'''
##
##'''
##
##s1 = {1,2,3,4,5}
##print(id(s1))
##
##l = list(s1)
##print(l)
##print(id(l))
##
##l[0] = 100
##
##s1 = set(l)
##print(s1)
##
##
##
##'''ADD'''
##
##s = {1,2,3,4,4,5,5,5,6}
##
##s.add(267)
##print(s)
##
##del s
##print(s)
##
##
##
##s = {1,2,3,4,4,5,5,5,6}
##
##s.remove(4)
##print(s)
##
##s.remove(34)
##print(s)
##
##s = {1,2,3,4,4,5,5,5,6}
##
##s.pop()  #pop() takes no argument
##print(s)
##
##s2 = {1,2,3,4,4,8,39,6}
##
##print(s+s2)
####
##print(s*2)
##
##
##'''
##LOOPING
##'''
##
##for i in s:
##    print(i)
##
##'''
##MEMBERSHIP
##'''
##
##print(39 in s2)
##
##s.update(s2)
##print(s)
##
##s = {1,2,3,4,4,5,5,5,6}
##print(s)
##
##'''
##In-built Functions
##'''
##
##print(len(s))
##
##print(min(s))
##
##print(max(s))
##
##print(sum(s))
##
##print(sorted(s))
##
##print(reversed(s)) # Set is Irreversible
##
##print(sorted(s,reverse = True))
##
##
##'''
##SETS METHODS
##'''
##
##seta = {1,2,3,22,2,3,2,3,"a",True,(6,7,8,0)}
##print(seta)
##
##
##setb = {21,2,3,54,99,"c"}
##print(setb)
##
##'''
##.add(): adds an element to the set
##'''
##seta.add(50) # arguments: only one
##print(seta) 
##
##
##'''
##.clear(): clears the element present in the set
##'''
##
##
##seta.clear() 
##print(seta) #results in empty set
##print(type(seta))
##
##
##seta = {1,2,3,22,2,3,2,3,"a",True,(6,7,8,0)}
##print(id(seta))
##
##
##'''
##.copy(): creates a copy of a set
##'''
##
##
##c = seta.copy() 
##print(c)
##print(id(c))
##
##
##
##'''
##set.difference() & set.difference_update()
##------------------------------------------
##
##.difference(): Return a set that contains the items that only exist in first set,
##               and not in second set.
##
##Meaning: The returned set contains items that exist only in the first set,
##         and not in both sets.
##
##SYNTAX: set.difference(set)
##'''
##
##setd = {1,2,2,2,3,4,4,3,4,5,5,6,7,8,9,0}
##sete = {1,2,3,3,2,3,4,5,11,12,13,14,15}
##
##
##print(setd)
##print(sete)
##
##g = setd.difference(sete)
##print(g)    #elements common in both the sets get removed & uncommon elements get printed
##print(setd) #original set remains unchanged
##
##
##'''
##.difference_update(): Remove the items that exist in both sets
##
##SYNTAX: set.difference_update(set)
##'''
##
##setd = {1,2,2,2,3,4,4,3,4,5,5,6,7,8,9,19}
##sete = {1,2,3,3,2,3,4,5,11,12,13,14,15}
##
##print(setd)
##print(sete)
##
##setd.difference_update(sete)
##print(setd)  # modified set
##
##
##
##'''
##NOTE: .difference() returns a new set, leaving the original sets unchanged,
##while .difference_update() modifies the calling set in place by removing common elements.
##'''
##
##
##'''
##.discrad(): removes an item from the set without throwing error message
##'''
##
##
##setd = {1,2,2,2,3,4,4,3,4,5,5,6,7,8,9,19}
##sete = {1,2,3,3,2,3,4,5,11,12,13,14,15}
##
##setd.discard(4)
##print(setd)
##
##
##'''
##.intersection(): Return a set that contains the items that exist in both sets.
##                 original set remains unchanged
##
##SYNTAX: set.intersection(set1, set2 ... etc)                 
##'''
##
##
##setd = {1,2,2,2,3,4,4,3,4,5,5,6,7,8,9,19}
##sete = {1,2,3,3,2,3,4,5,11,12,13,14,15}
##
##i = setd.intersection(sete)
##print(i)
##print(setd)
##
##j = sete.intersection(setd)
##print(j)
##print(sete)
##
##
##'''
##.intersection_update():
##
##SYNTAX: set.intersection_update(set1, set2 ... etc)
##'''
##
##setd = {1,2,2,2,3,4,4,3,4,5,5,6,7,8,9,19}
##sete = {1,2,3,3,2,3,4,5,11,12,13,14,15}
##
##sete.intersection_update(setd)
##print(sete)
##
##setd.intersection_update(sete)
##print(setd)
##
##
##
##'''
##.isdisjoint(): Return True if no items in first set is present in second set.
##'''
##
##setd = {1,2,2,2,3,4,4,3,4,5,5,6,7,8,9,19}
##sete = {1,2,3,3,2,3,4,5,11,12,13,14,15}
##
##
##print(setd.isdisjoint(sete))
##
##setf = {1,2,3,4,5}
##setg = {6,7,8,9,0}
##
##print(setf.isdisjoint(setg))
##
##
##'''
##.issubset(): Return True if all items in set x are present in set y
##'''
##
##x = {1,2,3,4,5,6,7,8}
##y = {3,2,4,6}
##
##print(y.issubset(x))
##
##print(x.issubset(y))
##
##
##'''
##.issuperset(): Return True if all items set y are present in set x.
##'''
##
##
##x = {1,2,3,4,5,6,7,8}
##y = {3,2,4,6}
##
##
##z = x.issuperset(y)
##print(z)
##
##Z = y.issuperset(x)
##print(Z)
##
##'''
##.pop(): Remove a random item from the set.
##'''
##
##x = {1,2,3,4,5,6,7,8}
##
##x.pop()
##print(x)
##
##m = x.pop()  #This method returns the removed item.
##print(m)
##
##
##'''
##.remove(): removes the specified element from the set.
##'''
##
##x = {1,2,3,4,5,6,7,8}
##
##x.remove(6)
##print(x)
##
##
##'''
##.symmetric_difference: Return a set that contains
##          all items from both sets, except items
##          that are present in both sets
##
##compliment of intersection
##'''
##
##x = {1,2,3,4,5,6,7,8}
##y = {3,2,4,6,9,0,11}
##
##print(x)
##print(y)
##
##u = x.symmetric_difference(y)
##print(u)
##print(x)
##
##w = y.symmetric_difference(x)
##print(w)
##print(y)
##
##
##'''
##.symmetric_difference_update() method updates the
##           original set by removing items that are present
##           in both sets, and inserting the other items.
##'''
##
##x = {1,2,3,4,5,6,7,8}
##y = {3,2,4,6,9,0,11}
##
##
##v = x.symmetric_difference_update(y)
##print(v)
##print(x) #updated set
##
##
##'''
##.union(): Return a set that contains all items from both sets,
##          duplicates are excluded
##
##SYNTAX: set.union(set1, set2...)
##'''
##
##x = {1,2,3,4,5,6,7,8}
##y = {3,4,6,9,0,11}
##
##print(x.union(y))
##print(x)
##
##
##print(y.union(x))
##print(y)
##
##
##z = {"a","abc","xz"}
##
##print(x.union(y,z))
##
##
##'''
##.update(): updates the current set, by adding items from another set
##           (or any other iterable).
##
##'''
##
##x = {1,2,3,4,5,6,7,8}
##y = {3,4,6,9,0,11}
##
##print(x)
##
##x.update(y)
##print(x) #updated set
##
##f = {1,2,3,2,3,2,4,4,6,4,7,8,9}
##print(f)
##
##g = {1,1,2,3,3,4,2,3,4,5,6,6,7,7,8,9,6,5,6655,6,6}
##print(g)
##
##f.symmetric_difference_update(g)
##print(f)
##
##g.symmetric_difference_update(f)
##print(g)
##
##
##
##
##s1 = {1,2,3,4,5,6,7,8,9,11,23}
##s2 = {1,2,3,4,5,3,2,2,9}
##
##print(s1.issubset(s2))
##print(s2.issubset(s1))
##
##
##print(s1.issuperset(s2))
##print(s2.issuperset(s1))
##
##
##'''task: create an employee detail. modify its address with your address? dictionary
##create am empty list,tuple,set,dictionary. print its type'''
##
##
##
##
##emp = {'name':"abc",'address':'123xyz'}
##print(emp)
##
##emp.update({'address':'xyz123'})
##print(emp)
##
##
##
##list1= []
##a = list()
##print(type(list1))
##print(type(a))
##
##t1 = ()
##print(type(t1))
##
##set1 = {()}
##print(type(set1))
##
##set2 = {''}
##print(type(set2))
##
##d1 = {}
##print(type(d1))
##
##
##
##
##'''
##what is a function()?
## function is a block of code with some purpose.
## it doesnt matter what we have written inside the function,
## what matter is all the input and the output.
##
##  after fun() it makes the task easier'
##
##ABSTRACTION- doesnt matter what is the code, what matters is just the output
##DECOMPOSITION- collection of function. ex:  making an application(login,logout,etc)
##
##COMPONENT  OF A FUNCTION:
##
##    def - define
##    function_name - identifier
##    (argument,parameter) -  input for function
##     Optional doc string
##     return - what to return
##    calling fun()
##
##'''
##
##
##def is_even(i):
##
##
##    x=i%2==0
##    print(x)
##    return x
##
##is_even(5)
##
##
##''' Function Types
##
##predefined(reserved,inbuilt)- print,int,input
##user-defined
##lambda
##
##definiton: set of block of codes
##
##
##SYNTAX:
##
##def fun_name()
##      stat/func body/logic
##  fun() calling of function
##  indentation rule- 4 spaces/1 tab
##
##  one fun() can be called multiple times
##  code of reusability
##
##
##'''
##
##
##def pubg(): #defining a function
##    print("hello")
##pubg()
##pubg()
##
##
##'''Function can be called multiple times'''
##
##
##
##
##'''sum of two numbers'''
##def add():
##    a = int(input('enter a number: '))
##    b = int(input('enter a number: '))
##    sum = a+b
##    print(sum)
##add()    
##'''-----------------------------------------------------------------------'''
##''' to check a number is odd or even'''
##def even_odd():
##    a = int(input("enter a number: "))
##    if a%2 == 0:
##        print(a, 'is even')
##    else:
##        print(a,'is odd')
##even_odd()       
##
##def add():
##    a = int(input('enter a number: '))
##    b = int(input('enter a number: '))
##    sum = a+b
##
##
##def add():
##    a=int(input("Enter number:"))
##    b=int(input("Enter number:"))
##    print ("sum is:",a+b)
##add()
##add()
##
##'''-----------------------------------------------------------------------'''
##
##def even():
##    a=int(input("Enter number:"))
##    if  (a%2==0):
##        print ("Enter number is Even.")
##    else :
##        print ("Enter number is odd.")
##even()
##even()
##
##'''-----------------------------------------------------------------------'''
##def check_even_odd():
##    x=int(input("Enter number:"))
##    if (x>0):
##        print ("Positive number.")
##        if (x%2==0):
##            print ("Even number")
##        else :
##            print ("Odd number")
##    elif (x==0):
##        print("Zero")
##    else:
##        print("negative number")
##        if (x%2==0):
##            print ("Even number")
##        else:
##            print ("Odd number")
##
##check_even_odd()
##'''-----------------------------------------------------------------------'''
##
##def add():
##    a = input('enter a number: ')
##    b = input('enter a number: ')
##
##    if not a.isdigit() or not b.isdigit():
##        print('enter integer values')
##        return
##
##    a = int(a)
##    b = int(b)
##    sum = a+b
##    print('the sum of a+b: ',sum)
##
##add()
##
##
##
##help('class')
##'''-----------------------------------------------------------------------'''
##
##print(fun_name.__doc__) # to read the doc.string of a user-defined function
##
##'''-----------------------------------------------------------------------'''
##'''Doc String'''
##
##def is_even(num):
##    '''
##        This fun() tells if a given number is even or odd
##        input: any valid integer
##        output: odd/even
##        created: Bhumika Gupta ma'am
##        last edited: 17 jan 2023
##    '''
##
##    if num%2==0:
##        return 'Even'
##    else:
##        return 'Odd'
##
##for i in range(1,11):
##    print(is_even(i))      #Function call
##print(is_even.__doc__)    
##
##
##
##'''-----------------------------------------------------------------------'''
##
##def add():
##    a = input('enter a number: ')
##    b = input('enter a number: ')
##
##    if not a.isdigit() or not b.isdigit():
##        print('enter integer values')
##        return
##                                                                  
##    a = int(a)
##    b = int(b)
##    sum = a+b
##    print('the sum of a+b: ',sum)
##
##add()
##'''-----------------------------------------------------------------------'''
##
##def bank():
##    user1 = 'nisha'
##    pin1 = '1234'
##
##    user2 = input('enter username: ')
##
##    if user1 == user2:
##        print('correct username')
##
##        pin2 = input('enter pin')
##
##        if pin2 == pin1:
##            print('login successful')
##
##            a1 = 1000
##            a2 = 5000
##            a3 = a1+a2
##            print('Amount Deposited: ',a3)
##
##            a4 = 100
##            a5 = a3 - a4
##            print('Balance Amount: ',a5)
##
##        else:
##            print('invalid pin')
##
##
##    else:
##        print('invalid username')
##        print('Do you want to continue? ')
##
##        check = input('yes or no')
##
##        if check == 'yes':
##            print('YES')
##        elif check == 'no':
##            print('NO')
##        else:
##            print('incorrect info')
##bank()
##            
##
##'''-------------------------------------------------------------------------------------'''
##
##def bank():
##    while True:    
##        user1 = 'nisha'
##        pin1 = '1234'
##
##        user2 = input('enter username: ')
##
##        if user1 == user2:
##            print('correct username')
##
##            pin2 = input('enter pin: ')
##
##            if pin2 == pin1:
##                print('login successful')
##
##                a1 = float(input('enter amount to be deposited: '))
##                a2 = float(input('enter amount to be deposited: '))
##                a3 = a1+a2
##                print('Amount Deposited: ',a3)
##
##                a4 = float(input('enter deducted amount: '))
##                a5 = a3 - a4
##                print('Balance Amount: ',a5)
##                print('Thank You for your visit.')
##
##
##                check = input('Do you want to continue? ').lower()
##
##                while check not in ['yes','no']:
##                    print("invalid input, Please enter yes or no")
##
##                    check = input('Do you want to continue? ').lower()
##                    
##                if check == 'no':
##                    print('Thank You for your visit.')
##                    break
##                
##
##            else:
##                print('invalid pin')
##
##        else:
##            print('invalid username')
##      
##            check = input('Do you want to continue? ').lower()
##
##            while check not in ['yes','no']:
##                print("invalid input, Please enter yes or no")
##
##                check = input('Do you want to continue? ').lower()
##                
##            if check == 'no':
##                print('Thank You for your visit.')
##                break
##bank()
##'''-----------------------------------------------------------------------'''
##
##
##def bank():
##    print('Welcome!')
##    Q = input('Do you want to deposit or withdraw?' ).lower()
##
##    while Q not in ['deposit','withdraw']:
##        print('invalid input')
##        print('please enter deposit or withdraw')
##
##        Q = input('Do you want to deposit or withdraw? ').lower()
##
##    if Q == 'deposit':
##        d = float(input("enter amount to be deposited: "))
##        print('amount deposited',d)
##
##    elif Q == 'withdraw':
##        w = float(input("enter amount to be withdrawn: "))
##        print('amount withdrawn',w)
##
##bank()
##'''--------------------------------------------------------------------'''
##
##
##def deposit():
##    a = float(input('Enter Balance Amount: '))
##    b = float(input('Enter Deposit Amount: '))
##
##
##    if a%b == 0:
##        a = a+b
##        print('Final Amount')
##    else:
##        print('Enter Correct value')
##
##
##def withdraw():
##    a = float(input('Enter Balance'))
##    b = float(input('Enter withdrawal Amount'))
##
##
##    if a >= b:
##        a = a-b
##        print('Insufficient Balance')
##
##
##print('1.Deposit','2.Withdraw')
##user= input('enter your choice: ').strip().lower()
##
##if user == 'withdraw':
##    withdraw()
##
##elif user == 'deposit':
##    deposit()
##else:
##    print('Incorrect Option')
##
##    
##task: should not exceed more than balance amount
##
##
##'''--------------------------------------------------------------------'''
##
##'''PARAMETERS vs ARGUMENTS'''
##
##'''
##ARGUMENTS: when we use function give any value.
##PARAMETERS: when creating function and expecting any value.
##
##ex: in
##
##
##
##
##
##default
##positional
##keywords
##arbitrary
##
##
##
##'''
##
##'''
##POSITIONAL ARGUMENTS:
##'''
##def power(a,b):
##    return a**b
##print(power(2,3))
##print(power(3,2))
##
##print(power(3)) #requires 2 arguments
##
##'''
##DEFAULT ARGUMENTS:
##'''
##def power(a=1,b=2):
##    return a**b
##print(power(2,4))
##print(power(4))
##
##
##'''
##ARBITRARY ARGUMENTS
##
##print(1,2,3,4,.....) #so what i can say here that print is very flexible
##function because it take as many as value.
##
##'''
##
##
##def flex(*a):
##    product = 1
##    print(number)  #output in tuple format
##
##    print(type(number))
##    for i in number:
##        product = product*i
##        print(product)
##
##flexi(1)
##flexi(1,2)
##flexi(1,2,3)
##flexi(1,2,3,4)
##        
##'''-----------------------------------------------------------------------------'''
##
##'''
##PRINT()
##'''
##
##it will print something which will be visible for user
##
##def func1(a,b):
##    c = a+b
##    print(c)
##
##func1(5,6)
##
##
##
##def func1(a,b):
##    c = a+b
##    print(c)
##
##output1 = func1(5,6)
##print(output1)
##
##
##
##
##'''
##https://pythontutor.com/visualize.html#mode=edit
##'''
##
##def func(x):
##    return x+1
##def func2(a,b):
##    c = a+b
##    return c
##output2 = func2(5,6)
##final_output = func(output2)
##print(final_output)
##
##
##def rem(x,y):
##    a = x%y
##    print(a)
##
##x = int(input('enter a number: '))
##y = int(input('enter a number: '))
##
##rem(x,y)
##
##
##def func(name,age):
##    print('my name is',name,'and i am',age,'years old')
##
##func('asus',8)    
##    
##    
##
##
##def add_numbers(a, b): 
##	return a + b 
##
##result = add_numbers(7, 9) 
##print(result) 
##
##'''
##GLOBAL AND LOCAL VARIBALE
##'''
##
##a = 15      #global variable
##def something():
##    a = 10
##    print('local',a)  #local variable
##
##something()
##print('gloabal',a)
##
##
##
##a = 15      #global variable
##def something():
##    a = 10
##    b = 0
##    print(b)
##
##something()
##print(b)
##print('global',a)
##
##
##'''
##SCOPE OF VARIBALES:
##local variable(s) can't be called outside function
##whereas global variables can be called inside and outside function.
##'''
##
##
##a = 15      #global variable
##def something():
##
##    global a  #global keyword
##    a = 10
##    print('local',a)  #local variable
##
##something()
##print('global',a)
##
##
##'''
##global KEYWORD:
##variable inside the function can be accessed outside
##the function by using the keyword global
##'''
##
##
##a = 15      #global variable
##def something():
##
##    global a  #global keyword
##    a = 10
##
##    global b
##    b = 0
##    print('local',a)   #local variable
##    print('local',b)
##    
##something()
##print('global',b)
##print('gloabal',a)
##
##'''print(global.__doc__) global is a keyword, not a func()'''
##
##help('global')
##
##
##a = 15
##
##def something():
##    global a
##    a = 10
##    x = globals()['a']
##    a = 11
##    print('local',a)
##
##something()
##print('global',a)
##
##
##'''
##globals()['varname']: helps in accessing the varivales(global) outside the function
##'''
##
##
##a = 15    #global variable
##
##def something():
##    global a       #updating global varibale with local variable
##    a = 10
####    x = globals()['a']
##    a = 11
##    print('local',a)
##
##something()
##print('global',a)
##
##
##
##
##a = 10    #global variable
##def local_scope():
##    a = 15   #local variable
##
##    def show():
##        print('inside func',a)
##
##    show()
##    
##local_scope()
##print('outside func',a)
##
##
##a = 10    #global variable
##def local_scope():
##    a = 15   #local variable
##
##    def show():
##        print('inside func',a)
##
##    show()
##    print('inside func',a)
##    
##local_scope()
##print('outside func',a)
##
##
##
##
##    
##
##
##a,b = 5,6
##
##def display():
##    if a<b:
##        c = a+b
##        print(c)
##
##display()
##
##
##a,b = 5,6
##
##def display():
##    if a<b:
##        c = a+b
##    print(c)
##
##display() 
##    
##        
##'''
##RECURSION: using of function inside a function
##
##function calling itself
##base case-termination
##recursion case -  calling itself(ex- factorial)
##'''
##
##
##def factorial(n):
##    if n == 0:
##        return 1
##    else:
##        return n*factorial(n-1)
##
##n = int(input('Enter a number: '))
##res = factorial(n)
##
##print(res)
##
##
##
##
##def palin(text):
##    if len(text)<=1:
##        print('palindrome')
##    else:
##        if text[0] == text[-1]:
##            palin(text[1:-1])
##        else:
##            print('not palindrome')
##
##
##palin('asdfdsa')
##palin('asddsa')
##palin('asdfgh')
##palin('malayalam')
##palin('malayalbm')
##
##
##'''---------------------------------------------------------------------------'''
##
##'''RECURSION FUNCTION'''
##
##function calling itself
##base case-termination
##Recursion case -calling itself(ex:-factorial)
##
##def factorial(n):
##    if n == 0:
##        return 1
##    else:
##        return n * factorial(n - 1)
##
##n = int(input("Enter a value for n: "))
##res = factorial(n)
##print(res)
##
##str=input("enter string :")
##rev_string=""
##
##for char in str:
##    rev_string=char+rev_string
##print("Reverse of give string",str,"is",rev_string)
##if str==rev_string:
##    print(str,"is palindrome")
##else:
##    print(str,"is not palindrome")
##
##def palin(text):
##    if len(text)==1 or len(text)==0:
##        print("palindrome")
##    else:
##        if text[0]==text[-1]:
##           palin(text[1:-1])
##        else:
##            print("not palindrom")
##palin("madam")
##palin("naan")
##palin("121")
##palin("1234")
##palin("malayalam")
##
##num=int(input("a"))
##print(type(str(num)))
##
##num = int(input("enter a number here:-"))
####order=len(str(num))
####sum = 0
##temp = num
##
##while temp > 0:
##    digit = temp % 10
##    cube = digit ** order
##    sum = sum + cube
##    temp = temp // 10  
##if sum == num:
##    print("It is an Armstrong number")
##else:
##    print("It is not an Armstrong number")
##
##n = int(input("Enter number: "))
##x = n
##rev = 0
##
##def prime(m):
##    flag = 0
##    for i in range(2, m):
##        if m % i == 0:
##            flag = 1
##            break
##    if flag==1:
##        return 0
##    else:
##        return 1
##
##while x > 0:
##    r = x % 10
##    rev = rev * 10 + r  # Fix the calculation of the reversed number
##    x = x // 10
##
##if prime(n) and prime(rev):
##    print(n, "is a Twisted prime")
##else:
##    print(n, "is not a twisted prime")
##
##def a  (x):
##    if x == 1:
##        print ('Byee',x)
##    else:
##        print('Hello',x)
##        a(x-1)
##a(10)
##
##
##def a  (x):
##    if x != 10:
##        
##        print('Hello',x)
##        a(x+1)
##    else:
##        print ('Byee',x)
##        
##a(1) 
##
##
##
##'''HOMEWORK'''
##1. Get number from user a tempreature value as degree fareheit and convert it into celsius using function
##2. Get number from user and find it's factorial using function with argument and one without argument and
##again do this with return and recursion value for both questions.
##
####Global and local Variable's Scope
##
##global_variable = 42
##another_global = "hello"
##
##all_globals = globals()
##
##print(all_globals)
##
##a=15
####a=23
##
##def something():
####    global a
##    a=12
##    print("this is in function",a)
##    
##    
##something()
##print("this is out function",a)
##
##
##Benefits of using a Function:
##1. Every code is self-contained and used to break up the entire login into
##pieces(Code Modularity)
##2. Works on the philosophy of write once use forever!(Code Reusability)
##3. Code is organized and coherent(Code Readability)##debugging make easy
##
##rabit problem(fibonacci problem)
####more time complexity
##import time
##def fib(m):                                             
##    if m == 0 or m == 1:
##        return 1
##    else:
##        return fib(m-1) + fib(m-2)
####start = time.time()
##print(fib(50))
####print(time.time()-start)
####
##dynamic programming (memoizetion(time <space))
##
####import time
##def memo(m,d):
##    if m in d:
##        return d[m]
##    else:
##        d[m]= memo(m-1,d) + memo(m-2,d)
##        return d[m]
##    
####start = time.time()
##d={0:1,1:1}
##print(memo(50,d))
####print(time.time()- start)
####print(d)
##
##
##'''
##LAMBDA FUNCTION
##'''
##'''lambda/anonymous function-- def--no,  syntax: lambda argument:expression,
##    function object'''
##
##
##x = lambda x: x**3
##result = x(9)
##print(result)
##
##
## Difference
## 1. Lambda has no return value
##print(type(x))
## 2. One line
## 3. Not used for code reusability
##4. No name
##
## Why?
## Along with Higher order functions
##higher order function are those function how require function as a input for thier work
##or a fuction return statement itself return function.
##
##b = lambda x: x[0] == 'a'
####print(b('applw'))
##print(b('bpplw'))
##
##b = lambda x: "Even" if x%2 == 0 else "Odd"
##print(b(3))
##
##def return_sum(L):
##    even_sum = 0
##    odd_sum = 0
##    
##    for i in L:
##        if i % 2 == 0:
##            even_sum = even_sum + i
##        if i % 2 != 0:
##            odd_sum = odd_sum + i
##    
##    return (even_sum, odd_sum)
##
##L = [11, 14, 21, 23, 56, 78, 45, 29, 28]
##
##even_sum, odd_sum = return_sum(L)
##
##print("Sum of even numbers:", even_sum)
##print("Sum of odd numbers:", odd_sum)
####
##
##
##
##def return_sum(func, L):
##    result = 0
##    for i in L:
##        if func(i):
##            result = result + i
##    return result
##L = [11,14,21,23,56,78,45,29,28]
##x = lambda x: x%2 == 0
##y = lambda x: x%2 != 0
##z = lambda x: x%3 == 0
####print(return_sum(x, L))
####print(return_sum(y, L))
##print(return_sum(z, L))
##
##
##map()
##filter()
##reduce()
##only those data on with we can perform loop()
##map
##L=[1,2,3,4,5,6]
##print(map(lambda x:x*2,L))
##
##print(list(map(lambda x:x*2,L)))
##
##print(list(map(lambda x:x%2==0,L)))
##
##
##students = [
##{
##    "name" : "Jacob Martin",
##    "father name" : "Ros Martin",
##    "Address" : "123 Hill Street",
##    },
##{
##    "name" : "Angela Stevens",
##    "father name" : "Robert Stevens",
##    "Address" : "3 Upper Street London",
##    },
##{
##    "name" : "Ricky Smart",
##    "father name" : "William Smart",
##    "Address" : "Unknown",
##    }
##]
##print(map(lambda student: student['name'],students))
##
##print(list(map(lambda student: student['name'],students)))
##
##
##Filter
##L=[1,2,3,4,5,6]
##print(list(filter(lambda x:x>=4,L)))
##
##fruits=['Apple','Orange','Mango','Guava','cherry']
##print(list(filter(lambda fruit:'e' in fruit,fruits )))
##
##Map vs ##Filter
##work on every item vs ##works on filered condition
##
##Reduce ##reduce the list
##import functools
##L=[1,2,3,4,5,6,7]
##print(functools.reduce(lambda x,y:x+y,L))
##
##
##L=[11,21,31,41,51,61,71]
##L=[11,21,31,41,71,51,61,]
##print(functools.reduce(lambda x,y:x if x<y else y,L))
##
##
##def fib(n):
##    a=0
##    b=1
##    c=a+b
##    if n<0:
##        print(n,"is nagative number")
##    else:
##        print(a)
##        print(b)
##        for i in range(2,n+1):
##            c=a+b
##            a=b
##            b=c
##            c=a+b
##            print(c)
##    return(c)
##print()
##fib(n)    
##
##
##
##
##'''GUI : Graphical User Interface'''
##
##import tkinter
##
####window = tkinter.Tk()
####
####window.mainloop()
##
##
###creating simple button
##
##def hello():
##    print('hello world')
##
##
##window = tkinter.Tk()
##
###here background overwrites bg
##button = tkinter.Button(window,text = 'Hello World',command = hello,bg = 'blue',background = 'white',fg = 'black')
##
### side-top,bottom,left,right, padding, 
###button.pack(side = 'top',expand = True)
##button.pack(side = 'top',padx = 25, pady = 50,expand = True)  
##
##window.mainloop()
##
##
##'''LABEL,BUTTON,ENTRY : INPUT FIELD'''
##
##import tkinter
##
##def hello():
##    print('Hello World')
##
##
##if __name__ == '__main__':
##    window = tkinter.Tk()
##    window.title('Tkinter First App')
##    window.geometry('700x500')   #width x height
##
##    label = tkinter.Label(window,text = 'WELCOME',bg = 'yellow')  #parent is window
##
##    label.pack() #show element on the position
##
##    button = tkinter.Button(window,text = 'Hello World',command = hello) #function call
##    button.pack()
##
##    window.mainloop()
##
##    print('The End') #will get printed while closing the window
##    
##    
##    
##
##'''NESTING'''
##
##import tkinter
##
##def hello():
##    print('Hello World')
##
##if __name__ == '__main__':
##    window = tkinter.Tk()
##    window.title('Tkinter First App')
##    window.geometry('700x500')
##
##    frame = tkinter.Frame(window)
##    frame.pack()
##
##    label = tkinter.Label(frame,text = 'Hello World')
##    label.pack()
##
##    button = tkinter.Button(frame,text = 'Hello World',command = hello)
##    button.pack()
##
##    window.mainloop()
##
##
##
##
##
##
##
##if __name__ == '__main__':
##    window = tkinter.Tk()
##
##    def printHello():
##        print(textentry.get())
##
##        
##    window.title('Tkinter First App')
##    window.geometry('700x1100')
##
##    label = tkinter.Label(window,text = 'Hello World',bg = 'red',fg = 'blue',height = 00,width = 15)
##    label.pack()
##
##      # state disables/enables the entry box
##    #textentry = tkinter.Entry(window,text = 'Hello',bg = '#fdbce1',state = tkinter.DISABLED)      
##    textentry = tkinter.Entry(window,text = 'Hello',bg = '#fdbce1',show = '*')
##    textentry.pack()
##
##
##        # button's background/foreground colour changes when pressed
##    button = tkinter.Button(window,text = 'Hello',bg = '#cdfe34',activebackground = 'orange',activeforeground = 'red',command = printHello)
##    button.pack()
##
##    
##
####
####
##for item in label.keys():
##    print(item,"",label[item])
####    print(button.keys())
##
####    print(label['width'])
####
####
##
##
##def computePrice():
##    totalprice = int(priceperitem_entry.get())*int(numberofitems_entry.get())
##    #Clears the entry before inserting the new value
##    totalprice_entry.delete(0, tkinter.END)
##
##    totalprice_entry.insert(0, str(totalprice))
##
##window = tkinter.Tk()
##window.title('Price Calculator')
##window.geometry('400x200')
##
##priceperitem_label = tkinter.Label(window, text = 'price per item')
##priceperitem_label.pack()
##
##priceperitem_entry = tkinter.Entry(window)
##priceperitem_entry.pack()
##
##
##numberofitems_label = tkinter.Label(window, text = 'no. of items')
##numberofitems_label.pack()
##
##numberofitems_entry = tkinter.Entry(window)
##numberofitems_entry.pack()
##
##
##totalprice_label = tkinter.Label(window, text = 'Total Price')
##totalprice_label.pack()
###totalprice_label.pack(side = 'left')
##
##totalprice_entry = tkinter.Entry(window)
##totalprice_entry.pack()
###totalprice_entry.pack(side = 'right')
##
##
##calculate_button = tkinter.Button(window, text = 'Calculate Total', command = computePrice)
##calculate_button.pack()
###calculate_button.pack(fill = 'x')
##
##
##
##
##
##window.geometry('700x500')    
##window.mainloop()



print(u"\U0001f600")
