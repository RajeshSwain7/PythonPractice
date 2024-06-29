# print("Program is started..")
#
# print(10/0) # ZeroDivisionError: division by zero
#
# print("Program is Completed..")


# try the same code with try & except method to handle the exception
print("Program is started..")
try:
    print(10/0)
except ZeroDivisionError:
    print("Enter in to Except block- Handled the Exception")

print("Program is Completed..")


# if there is no error then except block will be ignored
print("Program is started..")
try:
    print(10/5)
except ZeroDivisionError:
    print("Enter in to Except block- Handled the Exception")

print("Program is Completed..")

# when try condition through error while teh except block has different error mentioned then
# print("Program is started..")
# try:
#     print(10/0) #ZeroDivisionError
# except TypeError: # program will not execute as the actual exception nd except exception didn't not match
#
#     print("Enter in to Except block- Handled the Exception")
#
# print("Program is Completed..")

# add multiple except block in one code

print("Program is started..")
try:
    print(10/0) #ZeroDivisionError
except TypeError: # program will not execute as the actual exception nd except exception didn't not match
    print("Enter in to Except block- Handled TypeError")

except ZeroDivisionError: # program will not execute as the actual exception nd except exception didn't not match
    print("Enter in to Except block- Handled ZeroDivisionError")

print("Program is Completed..")

# Multi except blocks
#Statements under the else clause run only when no exception is raised.
#Statements in finally block will run every time no matter exception occurs or not.

# try:
#     <body>
# except <ExceptionType1>:
#     <Handler1>
# except <ExceptionTypeN>:
#     <HandlerN>
# except:
#     <handlerExcept>
# else:
#     <process_else>
# finally:
#     <process_finally>

#code:
try:
    num1, num2 = 10, 5
    result = num1 / num2
    print("Result is", result)
except ZeroDivisionError:
    print("Division by zero is error")
except SyntaxError:
    print("Comma is missing. Enter numbers separated by comma like this 1")
except:
    print("Wrong imput")
else:
    print("No Exception")
finally:
    print("This will execute no matter what")


#else
#case1-> Throw exception -> except will execute
#case2-> not throw exception -> else will execute if the statement not throw exception.

#finally:
#case1-> Throw exception -> except will execute
#case2-> not throw exception -> else will execute if the statement not throw exception.
#case3-> not throw exception -> finally will execute
#case4-> throw exception -> finally will execute

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
else:
  print("Nothing went wrong")
finally:
  print("The 'try except' is finished")

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
finally:
  print("The 'try except' is finished")

try:
  print(x)
except:
  print("Something went wrong")

finally:
  print("The 'try except' is finished")

#raise
# x = -1
# if x < 0:
#   raise Exception("Sorry, no numbers below zero")


#raise
def enterage(age):
  if age < 0:
    raise ValueError("Age cannot be negative")
  if age % 2 == 0:
    print("age is even")
  else:
    print("age is odd")


try:
  num = input("eneter the number")
  enterage(num)
except ValueError:
  print("negative values are not allowed")
except:
  print("something is wrong")
#using exception object
try:
  number = one
  print("this number is :", number)
except NameError as ex:
  print("Exception :", ex)  #Exception: name 'one' is not defined
