# if..else statement
a= 20
if a>15:
    print("true condition")
else:
    print("false condition")


# approch-1 print multiple statement

if True:
    print("this is true condition")
    print("this is true condition")
    print("this is true condition")
else:
    print("this is false condition")
    print("this is false condition")
    print("this is false condition")

# example-1 for even or odd

num = int(input("Enter a Number!: "))
if num% 2==0:
    print("Even Number!")
else:
    print("Odd Number!")

# approch-2 print multiple statement-2
if True:
    print("this is true condition")
    print("this is true condition")
    print("this is true condition")
else:
    print("this is false condition")
    print("this is false condition")
    print("this is false condition")

print("Out of if statement.....")


# single line conditional statement
# syntax-> statement/s if condition else statement/s

print("statement-1") if True else print("statement-2")

num2 = int(input("Enter a Number!: "))
print("Even Number") if num2%2==0 else print("ODD Number")

# Multiple statements with condition in single line
# syntax->  {statement/s, statement/s} if condition else {statement/s, statement/s}
{print("statement-1"), print("statement-2")} if False else {print("statement-3"), print("statement-4")}

# elif statement
# using elif we can add N number of condition.
'''Syntax:
    if condition:
        statement
    elif condition:
        statement
    elif condition:
        statement
    else:
        statement
 '''
# Example-1

a=50
if a==10:
    print("ten")
elif a==20:
    print("twenty")
elif a==30:
    print("thirty")
elif a==40:
    print("forty")
elif a==50:
    print("fifty")
else:
    print("Number is not in list...!")
