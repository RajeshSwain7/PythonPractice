num1= input("Enter a first number!:")
num2= input("Enter a second number!:")

print(num1+num2)  # as the input is in string , due to that when user print the addition value of num1 & num2,
# it did concatination instead of addition.
#output will be 5020


#to receive the proper addition value we have to do the type conversion
#approch-1

num3= int(input("Enter a first number!:"))
num4 = int(input("Enter a second number!:"))
print(num3+num4) #30+50 = 80


#approch-2
num5= input("Enter a first number!:")
num6= input("Enter a second number!:")

print(int(num5)+int(num6))


#approch-3 using float

num7= input("Enter a first number!:")
num8= input("Enter a second number!:")

print(float(num7)+float(num8))

