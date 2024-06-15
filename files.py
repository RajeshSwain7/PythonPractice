#file operation
# Opening & Closing Files
# ▪ Before reading/writing you first need to open the file. Syntax of opening a file is.
# f = open(filename, mode)
# ▪ After you have finished reading/writing to the file you need to close the file using close() method like
# this,
# f.close() # where f is a file pointer
# ▪ Different modes of opening a file are
# MODES DESCRIPTION
# "r" Open a file for read only
# "w" Open a file for writing. If file already exists its data will be cleared before
# opening. Otherwise new file will be created
# "a" Opens a file in append mode i.e to write a data to the end of the file

#open() & Close()
f = open('D:\Demofile\myfile.txt', 'w')  # open file for writting

f.write("this is my first line....\n")
f.write("this is my second line....\n")
f.write("this is my third line....\n")

f.close()

print("completed..")

#read() & readline()

 #open file for read
print(f.read()) #read entire content from the file
f.close()
print("completed...")
print("-------------------------------")
f = open('D:\Demofile\myfile.txt', 'r')
print(f.readlines()) #read entire content from the file
f.close()
print("completed...")

#append: To append the data you need to open the file in 'a' mode
f = open('D:\Demofile\myfile.txt', 'a')  # open file for append

f.write("this is my fourth line....\n")
f.write("this is my fifth....\n")
f.write("this is my sixth line....\n")

f.close()

print("completed..")

#Looping through the data using for loop
f = open('D:\Demofile\myfile.txt', 'r')
for l in f:
    print(l)
f.close()
print("completed..")