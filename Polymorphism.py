# Polymorphism->
class Parent:
    name = "scott"


class child(Parent):
    pass


c = child()


# print(c.name) # we can access the name variable from the child class using the object c.
# Polymorphism->
class Parent:

    def __init__(self, name):
        self.name = name

    def display(self):
        print("name is", self.name)


class child(Parent):

    def __init__(self, name, age):
        self.age = age
        Parent.__init__(self, name)

    def display(self):
        print("age is", self.age)


c = child("scott", 20)
c.display()


# overriding->
class Parent:
    name = "Scott"


class child(Parent):
    name = "Jack"  # override the existing value


c = child()
print(c.name)
# to print the name of the parent class
d = Parent()
print(d.name)


# overriding->
class Bank:
    def rateOfInterest(self):
        return 0;


class ICICI(Bank):
    def rateOfInterest(self):
        return 10.5;


class AXIS(Bank):
    def rateOfInterest(self):
        return 15.5;


i = ICICI()
print(i.rateOfInterest())
a = AXIS()
print(a.rateOfInterest())


# e.g
class c1:
    def m1(self):
        print("this is m1 from c1")


class c2(c1):
    def m1(self):
        print("this is m1 from c2")


class c3(c2):
    def m1(self):
        print("this is m2 from c3")


c = c3()
c.m1()  # it will call the latest class

# to call the c2 m2 we have to craete an object of c2
c = c2()
c.m1()


# over loading
class Human:
    def SayHello(self, name=None):
        if name is not None:
            print("Hello " + name)
        else:
            print("Hello")


h = Human()
h.SayHello()
h.SayHello("Rajesh")


# e.g
class Bird:
    def fly(self, name=None):
        if name == "Parrot":
            print("Parrot can fly")
        if name == "penguin":
            print("penguin can't fly")
        if name is None:
            print("no input")


obj = Bird()
obj.fly()
obj.fly("Parrot")
obj.fly("penguin")


# Encapsulation
class myClass:
    __a = 10  # private variable->  can only access within the method

    def dis(self):
        print(self.__a)


obj = myClass()
obj.dis()


# print(obj.__a) error

# e.g
class myClass:
    def __disp1(self):  # private method
        print("This is display method1")

    def disp2(self):  # public/ normal method
        print("This is display method2")
        self.__disp1()  # private method can be called within the public method


obj1 = myClass()
# obj1.disp1() #error because it is private
obj1.disp2()

# abstract class:
from abc import ABC, abstractmethod


class A(ABC):

    @abstractmethod
    def display(self):
        pass


class B(A):
    def display(self):
        print("welcome to Python....")


ob = B()
ob.display()

# E.g
from abc import ABC, abstractmethod  # import predefind python method


class Animal(ABC):
    @abstractmethod  # qualifier
    def move(self):  # abstract method
        pass


class Human(Animal):  # inheriting the abstract class
    def move(self):  # abstract method in child class
        print("I can walk and run")


class Snake(Animal):  # inheriting the abstract class
    def move(self):  # abstract method in child class
        print("I can crawl")


class Dog(Animal):  # inheriting the abstract class
    def move(self):  # abstract method in child class
        print("I can bark")


class Lion(Animal):  # inheriting the abstract class
    def move(self):  # abstract method in child class
        print("I can roar")


obj = Human()
obj.move()
obj1 = Snake()
obj1.move()
obj2 = Dog()
obj2.move()
obj3 = Lion()
obj3.move()

# e.g
from abc import ABC, abstractmethod


class X(ABC):
    @abstractmethod
    def m1(self):
        pass

    @abstractmethod
    def m2(self):
        pass


class Y(X):
    def m1(self):
        print("this is m1")

    def m2(self):
        print("this is m2")


class Z(Y):
    def m1(self):
        print("this is m1")

    def m2(self):
        print("this is m2")


on = Z()
on.m1()
on.m2()

# class with a constructor along with abstract method

from abc import ABC, abstractmethod


class A(ABC):
    def __init__(self):
        print("this is a constructor")

    @abstractmethod
    def display(self):
        pass


class B(A):
    def display(self):
        print("this is display")


ob = B()
ob.display()

# e.g
from abc import ABC, abstractmethod


class Cal(ABC):
    def __init__(self, value):
        self.value = value

        @abstractmethod
        def add(self):
            pass

        @abstractmethod
        def sub(self):
            pass


class Cal1(Cal):
    def add(self):
        print(self.value + 100)

    def sub(self):
        print(self.value - 10)


b = Cal1(1000)
b.add()
b.sub()







