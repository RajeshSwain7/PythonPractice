# Looping / Iterative Statement
# For Loop
# range() -> range function is used to print the sequence of values
# syntax->
'''
with one value specified as argument:
range(argument)

with two parameter
range(start, end)

with three parameter
range(start, end, increment/decrement)

Note: to print the full range we have to use the list()
Syntax->
    list(range(one parameter)
    list(range(start, end))
    list(range(start, end, increment/decrement))
'''

# Example

print(range(10)) #0,10
print(range(0,10))  #0,10
print(list(range(0,10))) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(0,10, 2)))  #[0, 2, 4, 6, 8]

print(list(range(1,10, 2))) #[1, 3, 5, 7, 9]
print(list(range(10,1, -2))) # [10, 8, 6, 4, 2]

# for loop

for i in range(10):
    print(i)
for i in range(2,20,2):
    print(i)
for i in range(1,10,2):
    print(i)
for i in range(10,1,-1):
    print(i)

# while loop
i=6;
while i<7:
    print(i)
    i=i+1

a=7
while a<=7:
    print(a)
    a=a+1

b=10
while b>=1:
    print(b)
    b=b-1

print("------------------")


# break
j=1
while j<6:
    print(j)
    if j==3:
        break
    j=j+1

#using for

for i in range(1,10):
    if i==5:
        break
    print(i)
print("program is exit")

# continue
# with while
s=1
while s<6:
    s = s + 1

    if s==3:
        continue
    print(s)

# with for
for g in range(1,10):
    if g==5:
        continue
    print(g)
print("program is exit")
