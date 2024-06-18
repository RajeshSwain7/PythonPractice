#constructor-> special method which is automatically called when the object is created
class MyClass:

  def m1(self):
    print("this is normal method.....")

  def __init__(self):
    print("this is constructor method.....")


mc = MyClass()
mc.m1()

# converting local variable into class variable(Here method taking the arguments)


class MyClass:

  def values(self, val1,
             val2):  # local variable can only access with in the method
    print(val1)
    print(val2)
    self.val1 = val1  #create a new class variable self.val1, then assign the local variable val1 to self.val1 (class variable).
    self.val2 = val2

  def add(self):
    #print(val1 + val2)  # we can not access the local variable out side the method
    print(self.val1 + self.val2)  # access the class variable


vc = MyClass()
vc.values(10, 20)
vc.add()


# using the constructor to initialize the object
class MyClass:

  def __init__(self, val1,
               val2):  # local variable can only access with in the method
    print(val1)
    print(val2)
    self.val1 = val1  #create a new class variable self.val1, then assign the local variable val1 to self.val1 (class variable).
    self.val2 = val2

  def add(self):
    #print(val1 + val2)  # we can not access the local variable out side the method
    print(self.val1 + self.val2)  # access the class variable


vc = MyClass(100, 200)
vc.add()

#string constructor


# without __str__()
class Person:

  def __init__(self, name, age):
    self.name = name
    self.age = age


p1 = Person("John", 36)

print(p1)


# with __str__()
class Person:

  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"


p1 = Person("John", 36)

print(p1)


#deleting method -> --del--(self)
class Person:

  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

  def __del__(self):
    print("object deleted")


p1 = Person("Rajesh", 26)
print(p1)
del p1
#deleting object
#deleting class
#deleting class
