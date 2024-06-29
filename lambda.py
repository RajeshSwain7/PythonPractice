#lambda function/ anonymous function :
#syntax-> lambda arguments: expression
#normal function
def add(x, y):
  return x + y


print(add(10, 20))
#lambda function
add = lambda x, y: x + y


def add(x, y):
  return x + y


print(add(10, 20))

x = lambda a, b: a + b
print(x(10, 20))  #passing multiple arguments

x = lambda a: a + 10
print(x(5))  #passing single argument
