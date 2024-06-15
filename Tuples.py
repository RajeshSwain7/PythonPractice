#creating a tuple
#empty tuple
tup1 = ()
#tuple with number
tup2 = (1, 2, 3, 4, 5)
#tuple with mixed datatypes
tup3 = (1, "Hello", 3.4)
#tuple with string
tup4 = ("Hello", "World")
#tuple with list
tup5 = (["Hello", "World"])
#nested tuple
tup6 = ("mouse", [8, 4, 6], (1, 2, 3))
#printing the tuple
print(tup1)
print(tup2)
print(tup3)
print(tup4)
print(tup5)
print(tup6)

t6 = tuple("abc")  #tuple with string
print(t6)
t5 = tuple([1, 2, 3])  #tuple with list
print(t5)
#function of tuple
tup1 = (1, 2, 3, 4, 5)
print(tup1[0])
print(tup1[1])
print(tup1[2])
print(tup1[3])
print(tup1[4])
#negative indexing
print(tup1[-1])
print(tup1[-2])
print(tup1[-3])
print(tup1[-4])
print(tup1[-5])
#slicing
print(tup1[1:4])
print(tup1[2:])
print(tup1[:3])
#concatenation
tup1 = (1, 2, 3, 4, 5)
tup2 = (6, 7, 8, 9, 10)
tup3 = tup1 + tup2
print(tup3)
#repetition
tup1 = (1, 2, 3, 4, 5)
tup2 = tup1 * 3
print(tup2)
#deleting
tup1 = (1, 2, 3, 4, 5)
del tup1
#print(tup1)
#min() in tuple
tup1 = (1, 2, 3, 4, 5)
print(min(tup1))
#max() in tuple
tup1 = (1, 2, 3, 4, 5)
print(max(tup1))
#len() in tuple
tup1 = (1, 2, 3, 4, 5)
print(len(tup1))
#count() in tuple
tup1 = (1, 2, 3, 4, 5, 1, 1, 1)
print(tup1.count(1))

#tuple with loop

t1=(1,60,20,50,100,15,20)
for i in t1:
    print(i)

#list vs tuples

list=[10,20,30]
list[0]=100
print(list) #[100,20,30]

# tp=(10,20,30)
# tp[0]=100 #error
# print(tp)

tf=(10,20,30)
print(tf)
tf=(100,20,30)
print(tf)

