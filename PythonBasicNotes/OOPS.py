'''OOPs - Object Oriented Programming'''

##what is an object?
##any thing/instance of a class.
##An object is a thing that has attributes/properties and behaviour/motion.
##object is a physical entity.
##
##Examples:
##    chair- attributes: colour,thickness,material
##           behaviour: used for sitting,relaxing
##           
##    waterbottle- attributes: colour,material,height
##                 behaviour: to store water
##
##    smartphone- attributes: inches,speakers,touchscreen,camera,battery,
##                behaviour: calling,messaging,internet connectivity,entertainment,


'''CLASS'''

##blueprint/template which is followed by objects.
##Every class may have multiple instances/objects.
##class is a Logical structure with behaviour.
##
##Class can have attributes(data) and functions
##
##special function- def __func__/___dict__,__dir__ (has double underscore __)
##
##constructor- __init__ (initializer),self called
##             reference(through): self,any term - refers to the attributes and properties of the object.1w
##
##class object --create for calling of a class

'''
SYNTAX:

class className:
    def __init__(ref,attr1,...):
        code
    def user(ref,attr1,...):
        code
obj = className()
obj.user()
         
'''

##in a class we can define muliple functions
##a class can be called by its class object.



'''Declaring a class'''

##class bottle:
##    def __init__(self):  #constructor
##        self.length = '20cm'
##        self.colour = 'red'
##        self.capacity = '1 ltr'
##        self.shape = 'cylindrical'
##        print('this is initializer')
####        print(self.colour)
##
##    def user(self):
####        self.colour = 'black'
####        print(self.colour)
##        print(f'my waterbottle is of length {self.length}, with colour {self.colour} and shape {self.shape} of capacity of {self.capacity}')
##
##b = bottle()
##b.user()



##class pen:
##    def __init__(self):
##        self.height = '10cm'
####        self.bodycolour = 'brown'
####        self.shape = 'cylinder'
##        self.ink = 'blue'
##        self.type = 'ballpoint'
####        self.purpose = 'writing'
##        print(' this is a constructor')
##
##    def ballpoint(self):
##        self.purpose = 'writing'
##        print(f'this is a {self.ink} inked {self.type} of length {self.height} used for the purpose of {self.purpose} only')
##a = pen()
##a.ballpoint()              



##print('the is name',self.name,'its age is',self.age)
##wiz = parrot() #instantiate class
####print(wiz.age)
##wiz.define()
#####access the attributes
###call class
##p = parrot('wiz',52) #class constructor
##print(wiz.name,wiz.age)
#print(p.age)


'''
types/pillars in OOPs -- multiple classes
1) INHERITANCE: Code reusability
    a = single level inheritance- A --> B
    b = multi level- A & B-->C
    c = multilevel inheritance- A-->B-->C
'''

#single level
##class parent/super class/base class
##class child/derived class


#----Single level inheritance example----

##class father:
##    def func(self):
##        self.sname = 'chaudhary'
##        print(f'fathers surname is {self.sname}')
##
##class son(father):
##    def func1(self):
##        self.quality = 'reading'
##        print(f'fathers surname to son is {self.sname} and his quality is {self.quality}')
##            
##        
##s = son()
##s.func()
##s.func1()

'''---------------------------------------------------------------------------------------------------'''

'''types/pillars in OOP's -- multiple classes
    1=Inheritance:-Code Reusability
        a=single level Inheritance-A-->B
        b=multiple level-A & B--->C
        c=Multi-level Inheritance-A-->B-->C
        
    2=Polymorphism- Code Reusability
    3= Encapsulation-- Data Security/hiding'''
#single-level
##class Parent/#super class/Base class
##class Child/#sub class/Derived Class



#-------single- level  simple example-------------------------------------
##class father:
##    def func(self):
##        self.sname='chaudhary'
##        print(f'fathers surname is {self.sname}')
##class son(father):
##    def func1(self):
##        self.quality='reading'
##        print(f'fathers surname to son is {self.sname} and his quality is {self.quality}')
##s=son()
##s.func()
##s.func1()


#create a child class bus which will inherits all variables and methods of vehicles class?

###Multiple-level
#####Base class1
####a=56 #variable
##class Mother:
##    a=45 #class variable
##    mothername="" #class variable
##    def mother(self,attr):
##        print(self.mothername) #data member
######base class2
##class Father:
##    fathername=""
##    def father(self):
##        print(self.fathername)
##class Son(Mother,Father):
##    def parents(self):
##        print("Father from Father class is: ",self.fathername)
##        print("Mother from Mother class is: ",self.mothername)
######derived class code
##s1=Son()
##s1.fathername="Ganesh"
##s1.mothername="Kamla"
##s1.parents()

##Multi-Level
##class Grandfather:
##    def ownhouse(self):
##        print("This is Grandfather's(Owner) of the house")
##class Father(Grandfather):
##    def ownbike(self):
##        super().ownhouse()
##        print("This is my Father's Bike")
##class Child(Father):
##    def ownbooks(self):
##        super().ownbike()
##        print("This is Me(Son) with the book")
##o=Child()
##o.ownhouse()
##o.ownbike()
##o.ownbooks()

#Polymorphism:
####Polymorphism---feactures--Using a single function we can execute classes methods
##and datamemebers
#--poly-- many, morph-- forms
##+ , 6+67, 'y'+'t'
###----------------**-- multiple class and their method**---------------------------------------------
##
##print('t'+'y')
##print(7+6)
##class HDFC():
##    def __init__(self):
##        self.balance=10000
##        print("Constructor of HDFC")
##    def deposite(self):
##        amount=int(input("Enter user deposite amount: "))
##        self.balance=self.balance+amount
##        print("Your balance is: ",self.balance)
##    def withdraw(self):
##        am=int(input("Enter user withdraw amount: "))
##        self.balance=self.balance-am
##        print("Your balance is: ",self.balance)
##        
##class SBI():
##    def __init__(self):
##        self.balance=5000
##        print("Constructor of SBI")
##    def deposite(self):
##        amount=int(input("Enter user deposite amount: "))
##        self.balance=self.balance+amount
##        print("Your balance is: ",self.balance)
##    def withdraw(self):
##        am=int(input("Enter user withdraw amount: "))
##        self.balance=self.balance-am
##        print("Your balance is: ",self.balance)
##
##def ATM(card):#parameter
##    card.deposite()
##    
##    card.withdraw()

##h=HDFC()
##s=SBI()
##ATM(s)
##ATM(s)














    
