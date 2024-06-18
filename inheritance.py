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

#super ()
