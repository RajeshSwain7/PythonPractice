# Assign String to a Variable
a = "Hello"
print(a)

# Quotes Inside Quotes
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

# Multiline Strings
# using three double /single quote
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


b = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(b)


# syntax-2 to create string using object string

name1= str() # empty string with no value
name2= str("Welcome to Python") # string with value
print(name1)
print(name2)


# string immutable-> as soon as we change the value it will create a new ID
str1="Welcome"
str2="Welcome"
print(id(str1),id(str2)) #2999041113376 2999041113376
str2="welcome123"
print(id(str1),id(str2)) #2999041113376 2999041316592 (it is changed due to it is immutable)

#string concatenation(+)
a="welcomeq"
print(a+" to new part")

# * operator
b="Welcome!"
print(b*3)