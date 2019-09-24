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


- Polymorphism with a Function and objects
create a function that can take any object, allowing for polymorphism

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
   
    def type(self): 
        print("USA is a developed country.") 
  
def func(obj): 
    obj.capital() 
    obj.language() 
    obj.type() 
   
obj_ind = India() 
obj_usa = USA() 
   
func(obj_ind) 
func(obj_usa) 

New Delhi is the capital of India.
Hindi the primary language of India.
India is a developing country.
Washington, D.C. is the capital of USA.
English is the primary language of USA.
USA is a developed country.