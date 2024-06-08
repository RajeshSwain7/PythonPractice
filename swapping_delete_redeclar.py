x = 10
y = 5
print("Before swapping", x, y)  #before swapping
x, y = y, x
print("after swapping", x, y)  # after swapping

# re-declaration

a = 100
print(a)
a = 5
print(a)

z = 673
print(z)

del z  # delete the variable
print(z)  # Name error
