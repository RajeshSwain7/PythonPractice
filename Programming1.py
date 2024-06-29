# how to print Fibonaci Series
# 0 1 1 2 3 5 8 13 21 34

n1=0
n2=1

print(n1)
print(n2)
for i in range (2,10):
    s=n1+n2
    print(s)
    n1=n2
    n2=s

#sum of Elements in Array

# input: arr[]={1,2,3}
# output: 6
# 1+2+3=6

arr=[1,2,3,4,5,6]
print(sum(arr)) # 21
print(sum(arr,10)) #31 (adding)
print(sum(arr,-10)) #11 (substracting)

# find the minimum and maximum value of Array

arr=[10,30,40,60,100,70]

max=arr[0]
n=len(arr)
# to print the maximum element
for i in range(1,n):
    if arr[i]>max:
        max=arr[i]
print(max)
# to print minimum element
min=arr[0]
n=len(arr)
for i in range(1,n):
    if arr[i]<min:
        min=arr[i]
print(min)

# how to find the length of list
#approch-1
myList=[1,4,5,6,7,8,3]
count=0
for i in myList:
    count=count+1
print("Length of myList is: ", count)

#approch-2
myList=[1,4,5,6,7,8,3,100,3]
print("Length of myList using len() is:", len(myList))

# swap first and last elements in a list
# in=[12,35,9,56,24]
# op=[24,35,9,56,12]

# in[1,2,3]
# op=[3,2,1]

# Approch-1,using temporary variable

myList=[12,39,9,54,24]
size=len(myList)

temp = myList[0] # store the index 0 value in teamp
myList[0]=myList[size-1] # store the last value in index 0
myList[size-1]=temp

print("List after swapping:", myList) #[24, 39, 9, 54, 12]

# approch -2
myList=[12,39,9,54,24]
myList[0], myList[-1] = myList[-1], myList[0]
print("List after swapping:", myList) #[24, 39, 9, 54, 12]

# approch-3 using tuple variable

myList=[12,39,9,54,24]
get=(myList[-1], myList[0]) # packing 12 12
myList[0], myList[-1] = get # unpacking
print("List after swapping:", myList) #[24, 39, 9, 54, 12]

# approch-4  using * operator
myList=[12,39,9,54,24]
start, *middle, end = myList
print(start) # 12
print(*middle) # 39 9 54
print(end) # 24
myList=[end,*middle, start]
print("List after swapping:", myList) #[24, 39, 9, 54, 12]


# approch -5 using pop() built-in function
myList=[12,39,9,54,24] # index start from 0
first= myList.pop(0) #12
last= myList.pop(-1) #24
myList.insert(0,last)
myList.append(first)
print("List after swapping:", myList) #[24, 39, 9, 54, 12]

# swap any two element in the list
#approch -1
my=[23,19,55,90] # index start from 0
print(my)
pos1,pos2=1,3
my[pos1],my[pos2]=my[pos2], my[pos1]
print("List after swapping:", my)


# approch-2 using pop() built-in function

my=[23,19,55,90] # index start from 0
print(my)
pos1,pos2=1,3
first_ele=my.pop(pos1) #19
sec_ele=my.pop(pos2-1) #23 55 90

my.insert(pos1,sec_ele)
my.insert(pos2,first_ele)
print("List after swapping:", my)

# approch -3 using tuple
my=[23,19,55,90] # index start from 0
print(my)
pos1,pos2=1,3
get= (my[pos1],my[pos2])
my[pos2], my[pos1] = get
print("List after swapping:", my)

# how to remove the Nth occurence from a word of list
myList =["geeks","for","geeks"]
word="geeks"
count=0
n=2
for i in range(0, len(myList)):
    if (myList[i]==word):
        count=count+1
        if(count==n):
            del myList[i]
print("Upadted list:", myList) # ['geeks', 'for']

# if the count occurence delete after 3

sList =["geeks","for","geeks", "geeks", "geeks", "geeks"]
word="geeks"
count=0
n=3
for i in range(0, len(sList)-1):
    if (sList[i]==word):
        count=count+1
        if(count==n):
            del sList[i]
print("Upadted list:", sList) # ['geeks', 'for', 'geeks', 'geeks', 'geeks']


# how to find  an element in list
# approch-1 using looping
myele=[1,2,3,4,5,6,7,8]
ele=4
flang=0
for i in myele:
    if (i==ele):
        print("Element is found")
        flang=1
        break
if(flang==0):
    print("Element not found")

# using in operator
myele=[1,2,3,4,5,6,7,8]
ele=100
if (ele in myele):
    print("Element is found")
else:
    print("Element is not found")


# How to clear list
# approch -1 using clear()
mylist= [1,2,3,4,5,6]
print("Before clearing my list:", mylist) #[1, 2, 3, 4, 5, 6]
mylist.clear()
print("after clearing my list:", mylist) #[]

#approch-2 Initialize value with no value

mylist= [1,2,3,4,5,6]
print("Before clearing my list:", mylist) #[1, 2, 3, 4, 5, 6]
mylist=[] # reinitailalize
print("after clearing my list:", mylist) #[]

# approch-3 using "*=0" this method removes all elements from the list and make it empty
mylist= [1,2,3,4,5,6]
print("Before clearing my list:", mylist) #[1, 2, 3, 4, 5, 6]
mylist *=0 #delete list
print("after clearing my list:", mylist) #[]

# approch-4 using del
mylist= [1,2,3,4,5,6]
print("Before clearing my list:", mylist) #[1, 2, 3, 4, 5, 6]
del mylist[1:4] #  [1, 5, 6]
del mylist[:] #[]
print("after clearing my list:", mylist) #[]
