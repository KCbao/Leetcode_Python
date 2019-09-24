## What is OOPS?
- Object Oriented Programming system in which programs are considered as a collection of objects. 
- Each object contains data (attributes) and code (methods/procedures).
- an object's procedures that can access and often modify the data fields of the object.

## 2 . Write basic concepts of OOPS?
Following are the concepts of OOPS and are as follows:.
Abstraction.
Encapsulation. （封装）
Inheritance.
Polymorphism.

## 3. What is a class?
- a representation of a type of object. It is the blueprint/ plan/ template that describe the details of an object.
- e.g., rice cooker: attributes: color, brand, methods: cook rice, steam, keep warm

## 4. What is an object?
- Object is termed as an instance of a class 
- it has its own state, behavior and identity
- two objects created from the same class can have different attributes

## 5. What is Encapsulation?
- can restrict access to methods and variables. keeps both safe from outside interference and misuse
- Benefits of Encapsulation:
The fields of a class can be made read-only or write-only.
A class can have total control over what is stored in its fields.
The users of a class do not know how the class stores its data. A class can change the data type of a field and users of the class do not need to change any of their code.


- Methods:
public methods	Accessible from anywhere
private methods	Accessible only in their own class. starts with two underscores

class Car:
    def __init__(self):
        self.__updateSoftware()

    def drive(self):
        print('driving')

    def __updateSoftware(self):
        print('updating software')

redcar = Car()
redcar.drive()
#redcar.__updateSoftware()  not accesible from object.


- Variables:
public variables	Accessible from anywhere
private variables	Accesible only in their own class or by a method if defined. starts with two underscores

class MyClass: 
    # Hidden member of MyClass 
    __hiddenVariable = 0
    
    # A member method that changes  
    # __hiddenVariable  
    def add(self, increment): 
        self.__hiddenVariable += increment 
        print (self.__hiddenVariable) 
   
% Driver code 
myObject = MyClass()      
myObject.add(2) 
myObject.add(5) 
  
% This line causes error 
print (myObject.__hiddenVariable) 

2
7
Traceback (most recent call last):
  File "filename.py", line 13, in 
    print (myObject.__hiddenVariable)
AttributeError: MyClass instance has no attribute '__hiddenVariable' 

% Access hidden variable
myObject = MyClass()      
print(myObject._MyClass__hiddenVariable) 


## 6 . What is Polymorphism?
- means same function name (but different signatures) being uses for different types / forms.

- Polymorphism with Inheritance:  Method Overriding
class Bird: 
  def intro(self): 
    print("There are many types of birds.") 
      
  def flight(self): 
    print("Most of the birds can fly but some cannot.") 
    
class sparrow(Bird): 
  def flight(self): 
    print("Sparrows can fly.") 
      
      
obj_bird = Bird() 
obj_bird.intro() 
obj_bird.flight() 
There are many types of birds.
Most of the birds can fly but some cannot.

obj_spr = sparrow()  
obj_spr.intro() 
obj_spr.flight() 
There are many types of birds.
Sparrows can fly.


- Polymorphism with a Function and objects (i.e., Python uses "duck typing" for classes)
1. create a function that can take any object, allowing for polymorphism
2. Duck-typing: if it walks, quacks like a duck, then it is a duck
我们可以编写一个函数，它接受一个类型为"鸭子"的对象，并调用它的"走"和"叫"方法。在使用鸭子类型的语言中，这样的一个函数可以接受一个任意类型的对象，并调用它的"走"和"叫"方法。如果这些需要被调用的方法不存在，那么将引发一个运行时错误。

class India(): 
    def capital(self): 
        print("New Delhi is the capital of India.") 
   
    def language(self): 
        print("Hindi the primary language of India.") 
   
    def type(self): 
        print("India is a developing country.") 
   
class USA(): 
    def capital(self): 
        print("Washington, D.C. is the capital of USA.") 
   
    def language(self): 
        print("English is the primary language of USA.") 
  
def func(obj): 
    obj.capital() 
    obj.language() 
    obj.type() 
   
obj_ind = India() 
obj_usa = USA() 
   
func(obj_ind) 
New Delhi is the capital of India.
Hindi the primary language of India.
India is a developing country.

func(obj_usa)
Washington, D.C. is the capital of USA. 
English is the primary language of USA.
AttributeError: 'obj_usa' object has no attribute 'print'

New Delhi is the capital of India.
Hindi the primary language of India.
India is a developing country.
Washington, D.C. is the capital of USA.
English is the primary language of USA.
USA is a developed country.


## 7 . What is Inheritance?
Inheritance is a concept where one class shares the structure and behavior defined in another class. Ifinheritance applied on one class is called Single Inheritance, and if it depends on multiple classes, then it is called multiple Inheritance.

-  Check if inheritance exists?
class Base(object): 
    pass   # Empty Class 
class Derived(Base): 
    pass   # Empty Class 
  
% Driver Code 
print(issubclass(Derived, Base)) : True
print(issubclass(Base, Derived)) : False
  
d = Derived() 
b = Base() 
  
% b is not an instance of Derived 
print(isinstance(b, Derived)) # False
  
% But d is an instance of Base 
print(isinstance(d, Base))  # True

- Multiple inheritance:

class Base1(object): 
    def __init__(self): 
        self.str1 = "Geek1"
        print "Base1"
  
class Base2(object): 
    def __init__(self): 
        self.str2 = "Geek2"        
        print "Base2"
  
class Derived(Base1, Base2): 
    def __init__(self): 
          
        # Calling constructors of Base1 
        # and Base2 classes 
        Base1.__init__(self) 
        Base2.__init__(self) 
        print "Derived"
          
    def printStrs(self): 
        print(self.str1, self.str2) 
         
  
ob = Derived() : Based 1, Base 2, Derived
ob.printStrs() : ('Geek1', 'Geek2')


- Access parent class in a subclass

1. Use Parent class name

class Base(object): 
  
    # Constructor 
    def __init__(self, x): 
        self.x = x     
  
class Derived(Base): 
  
    # Constructor 
    def __init__(self, x, y): 
        Base.x = x  
        self.y = y 
  
    def printXY(self): 
       
       # print(self.x, self.y) will also work 
       print(Base.x, self.y) 


2. Using super()  
class Derived(Base): 
  
    # Constructor 
    def __init__(self, x, y): 
        super(Derived, self).__init__(x) 
        self.y = y 
  
    def printXY(self): 
       # Note that Base.x won't work here 
       # because super() is used in constructor 
       print(self.x, self.y) 
  
  
  ## 9. Define a constructor?
- used to initialize the state of an object, and it gets invoked at the time of object creation. Constructor must have no return type
- def __init__(self):
    # body of the constructor
- Types of constructors :
1. default constructor : doesn’t accept any arguments.
def __init__(self): 
2. parameterized constructor : takes arguments
def __init__(self, f, s): 
        self.first = f 
        self.second = s 


## 10. Define Destructor?
- Destructor is a method which is automatically called after the program ended or when all the references to object are deleted i.e when the reference count becomes zero, not when object went out of scope.
- def __del__(self):
  # body of destructor

- class Employee: 
  
    # Initializing  
    def __init__(self): 
        print('Employee created') 
  
    # Calling destructor 
    def __del__(self): 
        print("Destructor called") 
  
def Create_obj(): 
    print('Making Object...') 
    obj = Employee() 
    print('function end...') 
    return obj 
  
print('Calling Create_obj() function...') 
obj = Create_obj() 
print('Program End...') 
Output:
Calling Create_obj() function...
Making Object...
Employee created
function end...
Program End...
Destructor called

## 12. What is operator overloading?
- giving extended meaning beyond their predefined operational meaning.
- e.g., operator + is used to add two integers as well as join two strings and merge two lists.
- 问题: add two objects with binary ‘+’ throws an error, because compiler don’t know how to add two objects. 
- fix: when use + operator, the magic method __add__ is automatically invoked in which the operation for + operator is defined
- We can overload all existing operators but we can’t create a new operator
- class A: 
    def __init__(self, a): 
        self.a = a 
  
    # adding two objects  
    def __add__(self, o): 
        return self.a + o.a  
ob1 = A(1) 
ob2 = A(2) 
ob3 = A("Geeks") 
ob4 = A("For") 
  
print(ob1 + ob2) : 3
print(ob3 + ob4) : Geeks For

## Abstract class
- considered as a blueprint for other classes, allows you to create a set of methods that must be created within any child classes built from your abstract class, 当subclass inherit parent class, it knows the structure of methods
from abc import ABC, abstractmethod 
class Animal(ABC): 
  
    def move(self): 
        pass
  
class Human(Animal): 
  
    def move(self): 
        print("I can walk and run") 
  
class Snake(Animal): 
  
    def move(self): 
        print("I can crawl") 
          
# Driver code 
R = Human() 
R.move() 
  
K = Snake() 
K.move() 
  
## 15. What is exception handling?
Exception is an event that occurs during the execution of a program. Exceptions can be of any type — Run time exception, Error exceptions. Those exceptions are handled properly through exception handling mechanism like try, catch and throw keywords.

## 16. Dynamic vs static typed language
Python is a dynamically-typed language. Java is a statically-typed language.

## Java versus Python
Compare between Java and Python.
Criteria	Java	Python
Ease of use	Good	Very Good
Speed of coding	Average	Excellent
Data types	Static typed	Dynamically typed
Data Science & machine learning applications	Average	Very Good