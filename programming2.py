# how to reverse the list
# approch-1 reverse()
mylist=[10,11,12,13,14,15]
print("mylist before reverse:", mylist) #[10, 11, 12, 13, 14, 15]
mylist.reverse()
print("mylist after reverse:", mylist) #[15, 14, 13, 12, 11, 10]

# approch-2 using slicing(:) technique [starting point: ending point]

mylist=[10,11,12,13,14,15]
print("mylist before reverse:", mylist) #[10, 11, 12, 13, 14, 15]
mylist2=mylist[::-1]
print("mylist after reverse:", mylist2) #[15, 14, 13, 12, 11, 10]

# how to clone or copy the list
# approch-1 using slicing technique
mylist=[10,11,12,13,14,15]
print("mylist before copy/clone:", mylist) #[10, 11, 12, 13, 14, 15]
mylistcopy=mylist[:]
print("mylist after copy/clone:", mylistcopy) #[10, 11, 12, 13, 14, 15]

# approch-2 using extend() method
my=[10,11,12,13,14,15]
print("mylist before copy/clone:", my) #[10, 11, 12, 13, 14, 15]
my_copy=[17,12]
my_copy.extend(my)
print("mylist after copy/clone:", my_copy) #[17, 12, 10, 11, 12, 13, 14, 15]

# approch-3 using list() method
my=[10,11,12,13,14,15]
print("mylist before copy/clone:", my) #[10, 11, 12, 13, 14, 15]
mylist_copy=list(my)
print("mylist after copy/clone:", mylist_copy) #[10, 11, 12, 13, 14, 15]

# approch-4 using copy() method
my=[10,11,12,13,14,15]
print("mylist before copy/clone:", my) #[10, 11, 12, 13, 14, 15]
mylist_copy=my.copy()
print("mylist after copy/clone:", mylist_copy) #[10, 11, 12, 13, 14, 15]

# approch-5 using list comprehension
my=[10,11,12,13,14,15]
myc=[i for i in my]
print(myc)  #[10, 11, 12, 13, 14, 15]


# count occurence of an element in a list
# approch-1 using loop
lt=[1,2,3,4,2,3,2,6,7,8,89,10,2,3,2]
x=2
count=0
for ele in lt:
    if(ele==x):
        count=count+1
print("{} has occured {} times".format(x,count)) #2 has occured 5 times

# approch-2 using count()
lt=[10,2,3,10,20,30,10,6,7,8,10,10,2,3,2]
x=10
print("{} has occured {} times".format(x,(lt.count(x)))) #10 has occured 5 times

# approch-3 using counter () method
from collections import Counter
lt=[10,2,3,10,20,30,10,6,7,8,10,10,2,3,2]
x=10
dic=Counter(lt)
print(dic) #Counter({10: 5, 2: 3, 3: 2, 20: 1, 30: 1, 6: 1, 7: 1, 8: 1})
print("{} has occured {} times".format(x,dic[x])) #10 has occured 5 times

# find the sum of elements in list

# approch-1 using loop with range()
mylist=[10,50,3,22]
total=0

for i in range (0,len(mylist)):
    total=total+mylist[i]
print("Sum of total element is:", total) #85

# approch-2 using sum()
mylist=[10,50,3,22]
sumof= sum(mylist)
print("Sum of total element is:", sumof) #85

# multiply all number in list
# approch-1 using loop with range()
mylist=[10,50,3,22]
multiply=1

for i in range (0,len(mylist)):
    multiply=multiply*mylist[i]
print("multiply of total element is:", multiply) #33000

# approch-2 using traversal
mylist=[10,50,3,22]
result=1

for i in mylist:
    result=result*i
print("Multiply of all element is :", result) #33000

# approch-3 using numpy.prod() * install numpy package
import numpy
mylist=[3,2,4]
result=numpy.prod(mylist)
print(result) # 24


# find the smallest and largest number of the list
# approch -1: sort the list in ascending order and print first & last element in the list

hhh=[20,100,20,1,0,10]
hhh.sort() #sorting
print(hhh) #[0, 1, 10, 20, 20, 100]

print("the samllest element of the list is: ", hhh[0]) #0
print("the largest element of the list id : ", hhh[5]) #100

# approch-2 min() & max() method
hhh=[20,100,20,1,0,10]
print("the samllest element of the list is: ", min(hhh)) #0
print("the largest element of the list id : ", max(hhh)) #100



