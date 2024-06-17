#creation of class and object which include methods
class Person:

  def myfunc(self):
    pass

  def user(self, name, age):
    print("Hello my name is " + name, "."
          "My age is " + age)


p1 = Person()
p1.myfunc()
p1.user("Rajesh", "26")

#instance method & static method
#instance method-> method which is called on the instance of the class


#static method-> method which is called on the class itself
#sysntax-> class_name.method_name()
#e.g
class MyClass:

  def m1(self):
    print("Instance Method....")

  @staticmethod  # to create a static method, we have to use the @staticmethod decorator / Identifier
  def m2():
    print("Static Method....")


mc = MyClass()  #object creation to call an instance method
mc.m1()  #calling instance method

MyClass.m2()  #calling static method using class name


#e.g
class Person:

  def myfunc(self):
    print("Hello there!!")

  @staticmethod
  def user(name, age):
    print("Hello my name is " + name, "."
          "My age is " + age)


p1 = Person()
p1.myfunc()

Person.user("Rajesh", "26")


#static method with parameter
#e.g
class Person:

  def myfunc(self):
    print("Hello there!!")

  @staticmethod
  def user(self):
    print(self)


p1 = Person()
p1.myfunc()
Person.user(100)


#Declaring variables inside the class
class MyClass:
  a, b = 10, 20

  def add(self):
    print(self.a + self.b)

  def mul(self):
    print(self.a * self.b)


cal = MyClass()
cal.add()
cal.mul()

# Local variable, class variables, and  Global variable
#e.g
i, j = 15, 25  #global variable


class MyClass:
  a, b = 10, 20  #class variable

  def add(self, x, y):  #local variable
    print(x + y)
    print(self.a + self.b)  #class variable
    print(i + j)  #global variable


cal = MyClass()
cal.add(100, 200)

# when all the variable are same

a, b = 15, 25  # global variable


class MyClass:
  a, b = 10, 20  #class variavle

  def add(self, a, b):  #local variable
    print(a + b)  #local variable
    print(self.a + self.b)  #class variable
    print(globals()['a'] + globals()['b'])  #global variable
    #globals() -> return all the global variables


#syantax-> globals()['variable_name']

cal = MyClass()
cal.add(100, 200)


#create multiple object for one class
class MyClass:

  def display(self):
    print("this is display method....")


obj1 = MyClass()
obj1.display()

obj2 = MyClass()
obj2.display()

#named object & nameless obeject


class MyClass:

  def display(self):
    print("this is display method....")


obj1 = MyClass()  # obj1 is the named object
obj1.display()

MyClass().display()  #nameless  obeject


#how to check memory location of object
class MyClass:

  def display(self):
    print("this is display method....")


c1 = MyClass()
c2 = c1
print(id(c1))
print(id(c2))

c3 = MyClass()
print(id(c3))
