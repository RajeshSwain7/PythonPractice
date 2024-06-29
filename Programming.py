# swapping the 2 number
# approch -1

num1=input("Enter the num1:")
num2=input("Enter the num2:")
print("value of num1 before swapping:" , num1)
print("value of num2 before swapping:" , num2)
num1,num2=num2,num1
print("value of num1 after swapping:" , num1)
print("value of num2 after swapping:" , num2)


# approch-2
num1=input("Enter the num1:")
num2=input("Enter the num2:")
print("value of num1 before swapping:" , num1)
print("value of num2 before swapping:" , num2)
temp=num1 #10
num1=num2 #20
num2=temp #10
print("value of num1 after swapping:" , num1)
print("value of num2 after swapping:" , num2)


# How to check a number is prime or not
# Natural Number >1
# Which has only 2 factor i.e. 1 & itself
# e.g 19 can be devisibale by 19 & 1 -< prime number
#28 can be divisible by 1,2,4,7,14,28-> not a prime number

num=int(input("Enter a Number:"))
count= 0 # to store the number of factor of a number define another variable

if num>1:
    for i in range(1,num+1):
        if (num%i)==0:
            count=count+1
    if count==2:
        print("Number is Prime.")
    else:
        print("Number is not a Prime Number")

# How to find a factorial of a Number
# num5 -> 1*2*3*4*5=120
# approch-1 interative/ looping approch

factorial = 1
num = int(input("Enter a Number"))

if num < 0:
    print("Factorial does not  exit for negative number")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1, num+1):
        factorial = factorial * i
    print("The Factorial of", num , "is", factorial)

# approch-2 (Recursion approch)

def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)

num = int(input("Enter a Number"))
print("The Factorial of", num , "is", factorial(num))

#turnary approch
def factorial(n):
    return 1 if  (n==0 or n==1) else n*factorial(n-1)
num = int(input("Enter a Number"))
print("The Factorial of", num , "is", factorial(num))