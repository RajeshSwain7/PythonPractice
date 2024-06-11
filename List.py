#creating list
list1 = []
list2 = list([10, 20, 30])  #list contains some value
list3 = [10, 20, 30, 40, 50]  # list contins value
list4 = ["john", "ram", "sam"]

print(list1)
print(list2)
print(list3)
print(list4)

#accessing list items
#we acn access the list using the index
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list[1])
print(list[2])
print(list[6])
print(list[-1])  #negative indexing
print(list[-3])

# common operation in list
list5 = [1, 2, 3, 4, 5, 6]
print(2 in list5)  # true if 2 is available in list
print(100 in list)  # false if 100 is not available in list.

#len()
list7 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(len(list7))  # 10

#max()
list8 = [2, 3, 4, 5, 6, 10, 12, 13, 50]
print(max(list8))  #50

#min()
list8 = [2, 3, 4, 5, 6, 1, 10, 12, 13, 50]
print(min(list8))  #1

#sum() -> it will sum the entire list
list12 = [4, 5, 6, 7, 8, 9, 1, 10, 50, 30]
print(sum(list12))  #130

#list slicing ->[start index: End Index]

listA = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(listA[2:5])  #13,14,15
#without specifying the last index
listA = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(listA[2:])  #listA =[13, 14, 15, 16, 17, 18, 19, 20]
#without specifying the starting index
listA = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(listA[:5])  #listA =[11,12,13, 14, 15]
print(listA[0:5])  #listA =[11,12,13, 14, 15]

#list concatination(+)
listb = [10, 20, 30, 40, 50]
listc = [2, 4, 5, 6]
listd = listb + listc
print(listd)  #[10,20,30,40,50,2,4,5,6]]

#* operator
listg = [10, 20, 3]
print(listg * 3)  #[10,20,3,10,20,3,10,20,3]]

list4 = [1, 2, 3, 4]
list5 = list4 * 3
print(list5)  # [1,2,3,4,1,2,3,4,1,2,3,4]]

#in, not in operator
list = [10, 20, 30, 40, 50]
print(10 in list)  #true
print(100 in list)  #false
print(15 not in list)  # true
print(70 not in list)  #true

#traversing list using for loop
# extract all value from list and print on eby one

list = [100, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in list:
  print(i)  # 100, 2, 3, 4, 5, 6, 7, 8, 9, 10

#Add value to list using append()
list = [1, 2, 3, 45, 5]
print(list)  #[1,2,3,45,5]
list.append(20)
print(list)  #[1,2,3,45,5,20]

#to chekc the repeated entry value, i.e. how many times it repeated using count()
list = [1, 2, 3, 4, 5, 6, 7, 8, 5, 45, 5]
print(list.count(5))  #3

#extend() -> to join two list
list1 = [20, 30, 40]
list2 = [40, 50, 60]
print(list1 + list2)  #[20,30,40,40,50,60]
list1.extend(list2)
print(list1)  #[20,30,40,40,50,60]
print(list1 + list2)  #[20,30,40,40,50,60,40,50,60

#extraction value from list
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list[3])  #4

#inster value to list using insert()
#syntax-> insert(insert value to the index: value to add)
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list)  #[1,2,3,4,5,6,7,8,9,10]
list.insert(3, 1001)
print(list)  #[1,2,3,1001,4,5,6,7,8,9,10]

#pop() -> to remove the value from the list
#Sysntx-> pop(index value)
fruits = ['apple', 'banana', 'cherry']

x = fruits.pop(1)
print(x)
#remove() -> to remove the value from the list
#syntax -> remove(value to remove)

fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")
print(fruits)

#reverse() -> to reverse the list
#syntax -> reverse()
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()  #['cherry', 'banana', 'apple']

#sort() -> to sort the list
#sysntax-> sort()
cars = ['Ford', 'BMW', 'Volvo']
cars.sort(reverse=True)
print(cars)  #['Volvo', 'Ford', 'BMW']


#Sort the list by the length of the values:
# A function that returns the length of the value:
def myFunc(e):
  return len(e)


cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(key=myFunc)
print(cars)  #['VW', 'BMW', 'Ford', 'Mitsubishi']

#sort the number
list = [20, 75, 50, 300, 100]
list.sort()
print(list)  #[20,50,75,100,300]

#clear()-> to clear the list
#syntax-> clear()
listr = [100, 20, 40]
listr.clear()
print(listr)

#copy()-> to copy the list
#syntax-> copy()
listk = [10, 14, 33]
listk.copy()
print(listk)

#list comprehension
for x in range(10):
  print(x)
list1 = [x for x in range(10)]
print(list1)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [x + 1 for x in range(10)]
print(list2)  #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list3 = [x for x in range(10) if x % 2 == 0]
print(list3)  #0, 2, 4, 6, 8]
