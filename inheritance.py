# what is inheritance:
# Classes can inherit the functionality of other classes.
# If an object is created using a class that inherits from a superclass,
# the object will contain the methods of both the class and the superclass.
# The same holds true for variables of both the superclass and the class that inherits from the superclass.
#Types of Inheritance
# ▪ Single
# ▪ Multi Level
# ▪ Hierarchical
# ▪ Multiple


#creating a Parent:
class Person:

  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)


#Use the Person class to create an object, and then execute the printname method:

x = Person("Rajesh", "Swain")
x.printname()


#create a child class:
#create a child class that inherits from the Person class:
class Student(Person):

  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of",
          self.graduationyear)


x = Student("Rajesh", "Swain", 2019)
x.welcome()

#to access the parent class from child class, the syntax is -> class class_name(parent_class_name):


class Parent:  #parent class

  def m1(self):
    print("this is m1 from class Parent")


class Child(Parent):  #child class

  def m2(self):
    print("this is m2 from class Child")


#to access parent class from child class, we have to create an object for child class.

obj = Child()
obj.m1()
obj.m2()


#single inheritance:
class A:
  x, y = 10, 20

  def m1(self):
    print(self.x + self.y
          )  # to access the class veriable we have to use the self keyword.


class B(A):
  a, b = 100, 200

  def m2(self):
    print(self.a + self.b)


#creating an object for the child class so that the child will inherited the property of the parent class.

obj = B()
obj.m1()
obj.m2()

# For the reusability purpose we can use the inheritance concept.
# Multi-Level inheritance:
# When a class inherits from another class, it is known as multi-level inheritance.


class A:
  x, y = 10, 20

  def m1(self):
    print(self.x + self.y
          )  # to access the class veriable we have to use the self keyword.


class B(A):
  a, b = 100, 200

  def m2(self):
    print(self.a + self.b)


class C(B):
  i, j = 15, 25

  def m3(self):
    print(self.i + self.j)


#object creation for the child class so that the child will inherited the property of the parent class.

obj2 = C()
obj2.m1()
obj2.m2()
obj2.m3()

#hierarchical inheritance:
#Hierarchical inheritance is a type of inheritance where multiple inheritance is used to create a new class that in


class A:
  x, y = 10, 20

  def m1(self):
    print(self.x + self.y
          )  # to access the class veriable we have to use the self keyword.


class B(A):
  a, b = 100, 200

  def m2(self):
    print(self.a + self.b)


class C(A):
  i, j = 15, 25

  def m3(self):
    print(self.i + self.j)


#object creation for the child class so that the child will inherited the property of the parent class.
obj1 = B()
obj1.m1()
obj1.m2()
obj2 = C()
obj2.m1()
obj2.m3()

#multiple inheritance:
#Multiple inheritance is a type of inheritance where more than one parent class is used to create a new class.
#syantax-> class class_name(parent_class_name1, parent_class_name2, parent_class_name3..)


class A:  #independent Parent
  x, y = 10, 20

  def m1(self):
    print(self.x + self.y)


class B:  #independent Parent
  a, b = 100, 200

  def m2(self):
    print(self.a + self.b)


class C(B, A):  #child which is inherided from it's Parent
  i, j = 15, 25

  def m3(self):
    print(self.i + self.j)


#object creation:
obja = C()
obja.m1()
obja.m2()
obja.m3()


#super():
#1. invoke parent class method:
#2. invoke parent class constructor:
#3. invoke parent class destructor:
#4. invoke parent class variable:
#5. invoke parent class function:
#1. invoke parent class method:
class A:

  def m1(self):
    print("this is m1 from class A")


class B(A):

  def m2(self):
    print("this is m2 from class B")
    super().m1()  # call parent calss method  i.e. m1()


obj = B()
obj.m2()


#2. invoke parent class constructor:
class A:

  def __init__(self):
    print("this is A constructor")


class B(A):

  def __init__(self):
    print("this is B constructor")
    super().__init__()  # call parent calss constructor  i.e. __init__()


obj = B()


#3. invoke parent class destructor:
class A:

  def __del__(self):
    print("this is A destructor")


class B(A):

  def __del__(self):
    print("this is B destructor")
    super().__del__()  # call parent calss destructor  i.e. __del__()


obj = B()


#4. invoke parent class variable:
class A:
  x, y = 10, 20


class B(A):
  a, b = 100, 200


obj = B()
print(obj.x, obj.y)
print(obj.a, obj.b)


class C:
  a, b = 100, 200


class B(C):
  i, j = 10, 20

  def m2(self, x, y):
    print(self.i + self.j)
    print(self.a + self.b)
    print(x + y)


obj = B()
obj.m2(1000, 2000)

# using super for the above example
a, b = 1000, 2000


class C:
  a, b = 100, 200


class B(C):
  a, b = 10, 20

  def m2(self, x, y):
    print(x + y)
    print(self.a + self.b)
    print(
        super().a + super().b
    )  # when the variable are override we have to use the super() keyword.
    print(globals()['a'] + globals()['b']
          )  # global variabl are used to access the global variable.


obj = B()
obj.m2(1000, 2000)


#5. invoke parent class function:
class A:

  def m1(self):
    print("this is m1 from class A")


class B(A):

  def m2(self):
    print("this is m2 from class B")
    super().m1()  # call parent calss function  i.e. m1()


obj = B()
obj.m2()

#super() with keyword arguments:


#E.g
class Person:

  def __init__(self, first, last):
    self.first = first
    self.last = last


class child(Person):

  def __init__(self, first, last, id):
    super().__init__(first, last)
    self.id = id

  def display(self):
    print("EMP Id: {} FirstName:{} LastName:{}".format(self.id, self.first,
                                                       self.last))


c = child("Rajesh", "Swain", "101")
c.display()

#with str method


#E.g
class Person:

  def __init__(self, first, last):
    self.first = first
    self.last = last


class child(Person):

  def __init__(self, first, last, id):
    super().__init__(first, last)
    self.id = id

  def __str__(self):
    return ("EMP Id: {} FirstName:{} LastName:{}".format(
        self.id, self.first, self.last))


c = child("Rajesh", "Swain", "101")
print(c)  #invoke __str__() method and print the value
