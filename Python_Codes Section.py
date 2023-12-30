#Single reusponsibility (SOLID)

# class Shape:
#     def area(self):
#         pass
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def area(self):
#         return self.width * self.height
# r = Rectangle(4, 5)
# print(r.area())


#Nested function

# def composition(y,x):
#     return y(y(x))  #composition
# def multip(x):
#     return x**2
# obj=composition(multip,2)
# print(obj)


# Shallow & deep copy

# a=[1,2,3,4,5]
# b=a.copy()   #shallow copy
# c=a        #deep copy
# b[0]=5
# c[0]=20  
# print(a)
# print(b)
# print(c)


#List Comprehension

# a={x for x in 'abcdefghijklmn'if x not in 'abcde'}    
# print(a)

#Setter

# class Customer:
#     def set_name(self,new_name):
#         self.name=new_name
#     def display(self):
#         print(self.name)
# x=Customer()
# x.set_name("Khaled")
# x.display()


#Magic functions as __str__ & __add__

# class Customer:
#     def	__init__(self, name, balance=0):  
#         self.name = name
#         self.balance = balance
#         print("The init method was called")
        
#     def __str__(self):
#         return 'Customer : ' +str(self.name)+ ' , balance: ' + str(self.balance) 
    
#     def __add__(self, other): 
#         return Customer(self.name,self.balance + other)
    
# cust=Customer("Khaled",20000000)
# print(cust.__str__())
# print(cust.__add__(50000))


#Just knowing that object is an built in method whether we write it or not

# class person(object):
#     def __init__(self,name,idnum):
#         self.name=name
#         self.idnum=idnum
#     def disp(self):
#         print("name:",self.name)    
#         print("id",self.idnum)
# per=person("Khaled",100)
# per.disp()


#Inheritance
# class persson(object):
#     def __init__(self,name,idnum):
#         self.name=name
#         self.idnum=idnum
#     def Disp(self):
#         print("name:",self.name)    
#         print(self.idnum)

# class Employee(persson):
#     def __init__(self,name,idnum,salary,post):
#         self.salary=salary
#         self.post=post
#         persson. __init__(self,name,idnum) 
#     def Display(self):
#         self.Disp()
#         print(self.post)
#         print(self.salary)
# r=Employee("Kh",70,1000000,890)
# r.Display()


#Multilevel inheritance

# class fir:
#     def __init__(self):
#         self.str1="hi"
#         return self.str1

# class sec:
#     def __init__(self):
#         self.str2="welcome"
#         return self.str2

# class plus(fir,sec):
#     def __init__(self):
#         fir.__init__(self)
#         sec.__init__(self)
#         print('plus')
#     def display(self):
#         print(self.str1,self.str2)

# obj=plus()
# obj.display()


#Protected Functions 

# class Father:
#     def __init__(self,name,age):
#         self._name=name
#         self._age=age
#     def _display(self):
#         print(f"my name is {self._name}")
#         print(f"my age is {self._age}")

# class child(Father):
#     def __init__(self,name,age,id):
#         super().__init__(name,age)
#         self._id=id
#     def _disp(self):
#         self._display()
#         print(f"My id is {self._id}")

# obj1=Father("Ahmed",45)
# obj1._display()
# obj2=child("Ali Ahmed",10,1)
# obj2._disp()

#Private Access

# class Father:
#     def __init__(self,name,age):
#         self.__name=name
#         self.__age=age
#     def __display(self):
#         print(f"my name is {self.__name}")
#         print(f"my age is {self.__age}")
#     def accesspriv(self):
#         self.__display()

# class child(Father):
#     def __init__(self,name,age,id):
#         super().__init__(name,age)
#         self.__id=id
#     def get_id(self):
#         return self.__id
#     def set_id(self):
#         self.__id=int(input("Enter your Id : "))

# obj1=Father("Ahmed",45)
# obj1.accesspriv()
# obj2=child("Ali Ahmed",10,1)
# print(obj2.get_id())

#An error occurs if we pass 2 args 

# def product(a,b):
#     p=a*b
#     print(p)

# def product(a,b,c):
#     p= a *b * c
#     print(p)

# product(1,2,6)


# Solution for that problem

# def add(a=None,b=None):
#     if a!=None and b==None:
#         print(a)
#     else:
#         print(a+b)
# add(2)


#Another Solution using Multipledispatch library

# from multipledispatch import dispatch

# @dispatch(int,int,int)
# def product(f1,s2,th3):
#     result=f1*s2*th3
#     print(result)

# @dispatch(float,float,float)

# def product(f1,s2,th3):
#     result=f1*s2*th3
#     print(result)

# product(10,1,3)
# product(10.0,1.0,4.0)

#Abstract Method --> (Interface in java)

# from abc import ABC , abstractmethod

# class polygon(ABC):
    
#     @abstractmethod
#     def numofsides(self):
#         pass

# class Circle (polygon):

#     def numofsides(self):
#         print("I have infinite sides") 

# class Triangle(polygon):
#     def numofsides(self):
#         print("I have 3 sides ")
    
# class Hexagon(polygon):

#     def numofsides(self):
#         print("I have 6 sides")
        

#Accessing inner function from outer function

# def f1():
#     print("that is f1")
#     def f2():
#         print("that is f2")
#     f2()
# f1()


#Error handling

# x=10
# y="hello"
# try:
#     z=x+y
# except TypeError:
#     print('It is a type error')

# def func(a):
#     if a<6:
#         b=a/(a-5)
#     print("value of b =",b)  
# try:
#     func(3)
#     func(5)
# except ZeroDivisionError:
#     print("Denomerator can not be divided by 0")  
# except NameError:
#     print("Name Error!!")


# class Parent(): 
# 	def __init__(self): 
# 		self.value = "Inside Parent"
	
# 	def show(self): 
# 		print(self.value) 
		

# class Child(Parent): 

# 	def __init__(self): 
# 		self.value = "Inside Child"
		 
# 	def show(self): 
# 		print(self.value) 
		
		
# obj1 = Parent() 
# obj2 = Child() 
# obj1.show() 
# obj2.show() 

# Class attribute accessing

# class Eng_Student:
# 	stream = 'cse'				
# 	def __init__(self,name,roll):
# 		self.name = name		 
# 		self.roll = roll		

# ob = Eng_Student('Geek', 1)
# obj = Eng_Student('Nerd', 2)

# print(ob.stream) 
# print(obj.stream) 
# print(ob.name) 
# print(obj.name) 
# print(ob.roll) 
# print(obj.roll) 

# print(Eng_Student.stream) 

# Eng_Student.stream = 'mech'

# print(ob.stream)
# print(obj.stream) 



class A(object): 
	def __init__(self, x): 
		self.x = x 
	
	def getX(self): 
		return self.X 
	
class B(object): 
	def __init__(self, x, y): 
		self.x = x 
		self.y = y 
	def getSum(self): 
		return self.X + self.y 



class C_A(A): 
	def isA(self): 
		return True
	
	def isB(self): 
		return False


class C_B(B): 
	def isA(self): 
		return False
	
	def isB(self): 
		return True

def getC(cond): 
	if cond: 
		return C_A(1) 
	else: 
		return C_B(1,2) 


ca = getC(True) 
print(ca.isA()) 
print(ca.isB()) 
	
cb = getC(False) 
print(cb.isA()) 
print(cb.isB()) 


class A(object): 
	def __init__(self, x): 
		self.x = x 
	
	def getX(self): 
		return self.X 


cond = True


class C(A if cond else object): 
	def isA(self): 
		return True

ca = C(1) 
print(ca.isA()) 

