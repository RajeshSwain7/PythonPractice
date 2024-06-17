#function
#empty function
def myfunction():  #function defination
  pass


myfunction()  #function calling


#funcation with arguments
def myfunction(fname):
  print(fname + " Refsnes")


myfunction("Emil")
myfunction("Tobias")
myfunction("Linus")


#function with multiple arguments
def myfunction(fname, lname):
  print(fname + " " + lname)


myfunction("Emil", "Refsnes")


#function with default arguments
def myfunction(country="Norway"):
  print("I am from " + country)


myfunction("Sweden")
myfunction("India")
myfunction()
myfunction("Brazil")


#e.g
def sum(start, end):
  result = 0
  for i in range(start, end + 1):
    result += i
  print(result)


sum(1, 10)
sum(10, 20)
sum(1, 5)


#function with return
def myfunction(x):
  return 5 * x


print(myfunction(3))
print(myfunction(5))
print(myfunction(9))

#return statement without the returning anything


def sum(start, end):
  if (start > end):
    print("start should be smaller than end")
    return  #return null
  result = 0
  for i in range(start, end + 1):
    result = result + i
  return result


print(sum(1, 5))
print(sum(5, 1))

#global variable vs local variable
#global variable-> variable declared outside the function
#local variable-> variable declared inside the function
#e.g
global_var = 10


def myfunction():
  local_var = 5
  print(local_var)
  print(global_var)


myfunction()
#global variable
x = 100
y = 200


def func():
  print(x)
  print(y)


func()
print(x)
print(y)
#local variable
x = 100
y = 200


def func():
  x = 50
  y = 60
  print(x)
  print(y)


func()
print(x)
print(y)
#e.g-?> make the local variable as global variable using global keyword
x = 100
y = 200


def func():
  # global x =10 invalid
  global x
  x = 50
  y = 60
  print(x)  # 50
  print(y)  # 60


func()
print(x)  #50
print(y)  #200


#e.g-?> make the local variable as a global variable using the global keyword
def func():
  global j
  j = 50
  z = 60
  print(j)  # 50
  print(z)  # 60


func()
print(j)  #50

#print(z)  #error while accessing the local variable outside the function


# different arguments in the method
#e.g
def myfunction(x, y):
  print(x)
  print(y)


myfunction(1, 5)
myfunction(5, 1)
myfunction(y=1, x=5)
myfunction(x=5, y=1)


#e.g
def myfunction(x, y, z):
  print(x)
  print(y)
  print(z)


myfunction(1, 5, 6)
myfunction(5, 1, 6)
myfunction(y=1, x=5, z=6)
myfunction(x=5, y=1, z=6)


#e.g with default arguments
def myfunction(x, y=5):
  print(x)
  print(y)


myfunction(1)
myfunction(1, 2)
myfunction(x=1, y=2)


def func(i=0, j=0):
  print(i, j)


func(20)  #20, 0 # 0 is the defult value of j


#keyword arguements/ named arguments
def named_arg(name, age):
  print(name, age)


named_arg(name="John", age=20)


#mixed arguments and keyword arguments
def mixed_arg(name, age, city):
  print(name, age, city)


mixed_arg(name="John", city="New York", age=20)
mixed_arg(age=30, city="New York", name="John")
#mixed_arg(age=30,40,city='New York') #error postional argument follows keyword argument
mixed_arg("john", 20, "New York")
mixed_arg(name="john", age=20, city="New York")


#returning multiple values
def bigger(a, b):
  if a > b:
    return a, b
  else:
    return b, a


print(bigger(10, 20))
print(bigger(20, 10))


#verify the return value type
def bigger(a, b):
  if a > b:
    return a, b
  else:
    return b, a


print(type(bigger(10, 20)))
