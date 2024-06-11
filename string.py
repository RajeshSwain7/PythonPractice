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

#slicing
#syntax-> [start Index : end index]
b = "Hello, World!"
print(b[2:5])
#syntax for slicing from first-> [:end index]
c = "Hello, World!"
print(c[:5])
# syntax for slicing from end-> [start index :]
d = "Hello, World!"
print(d[6:])
# negative index -> [- start Index : - end index]
g = "Hello, World!"
print(g[-5:-2])

#String modify

#upper()
z = "Hello, World!"
print(z.upper())

#lower()
j = "Hello, World!"
print(j.lower())
#remove whitespace
#strip()
e = " Hello, World! "
print(e.strip())  # returns "Hello, World!"

# replace()
f = "Hello, World!"
print(f.replace("H", "J"))

# split()
k = "Hello, World!"
print(k.split(","))  # returns ['Hello', ' World!']

# String Format
# syntax-> f{ }
age = 36
txt = f"My name is John, I am {age}"
print(txt)

#placeholder
# Add a placeholder for the price variable:

price = 59
txt = f"The price is {price} dollars"
print(txt)

#Display the price with 2 decimals:

price = 49
txt = f"The price is {price:.2f} dollars"
print(txt)
#Perform a math operation in the placeholder, and return the result:

txt = f"The price is {20 * 59} dollars"
print(txt)

#string function
#len(), min(), max()
print(len("abcde"))
print(min("abcde"))
print(max("abc"))

# string comparison
#using relational operator(==,>,<,>=,<=,>, !=)

print("tim" == "tee")  #false
print("free" != "freedom")  #true
print("arrow" > "areon")  #true
print("right" >= "left")  #true
print("teeth" < "tee")  #false
print("yellow" <= "fellow")  #flase
print("abc" > "")  #true

#retun Ascii &char using ord() and chr()
print(ord("A"))  #65
print(chr(65))  #A

#Sring with looping
s = "hello"
for i in s:
  # print(i)
  # print(s)
  # print(s, end="\n")
  # print(s, end="")

  #to append another value to s
  print(s, end="xyz")
#string testing Methods
# Sample string
sample_string = "Hello, World This is a test."

# Using capitalize()
capitalized = sample_string.capitalize()
print(f"Capitalized: {capitalized}")

# Using casefold()
lowercased = sample_string.casefold()
print(f"Lowercased: {lowercased}")

# Using center()
centered = sample_string.center(50)
print(f"Centered: {centered}")

# Using count()
count_example = sample_string.count("o")
print(f"Count of 'o': {count_example}")

# Using encode()
encoded = sample_string.encode('utf-8')
print(f"Encoded: {encoded}")

# Using endswith()
ends_with_hello = sample_string.endswith("World!")
print(f"Ends with 'World': {ends_with_hello}")

# Using expandtabs()
expanded_tabs = sample_string.expandtabs(20)
print(f"Expanded tabs: {expanded_tabs}")

# Using find()
find_hello = sample_string.find("World")
print(f"Find 'World': {find_hello}")

# Using format()
formatted = "{}, {}!".format(sample_string, "Python")
print(f"Formatted: {formatted}")

# Using format_map()
dict_values = {"first": "Hello", "second": "Python"}
formatted_map = formatted.format_map(dict_values)
print(f"Formatted map: {formatted_map}")

# Using index()
index_world = sample_string.index("World")
print(f"Index of 'World': {index_world}")

# Using isalnum(), isalpha(), isascii(), isdecimal(), isdigit(), isidentifier(), islower(), isnumeric(), isprintable(), isspace(), istitle(), isupper()
print(f"isalnum(): {''.join(filter(str.isalnum, sample_string))}")
print(f"isalpha(): {''.join(filter(str.isalpha, sample_string))}")
print(f"isascii(): {all(c.isascii() for c in sample_string)}")
print(f"isdecimal(): {all(c.isdigit() for c in sample_string)}")
print(f"isdigit(): {all(c.isdigit() for c in sample_string)}")
print(f"isidentifier(): {sample_string.isidentifier()}")
print(f"islower(): {all(c.islower() for c in sample_string)}")
print(f"isnumeric(): {all(c.isnumeric() for c in sample_string)}")
print(f"isprintable(): {all(c.isprintable() for c in sample_string)}")
print(f"isspace(): {all(c.isspace() for c in sample_string)}")
print(f"istitle(): {sample_string.istitle()}")
print(f"isupper(): {all(c.isupper() for c in sample_string)}")

# Using join()
joined = "-".join(["Hello", "World"])
print(f"Joined: {joined}")

# Using ljust()
left_justified = sample_string.ljust(50)
print(f"Left justified: {left_justified}")

# Using lower()
lower_cased = sample_string.lower()
print(f"Lower case: {lower_cased}")

# Using lstrip()
left_stripped = sample_string.lstrip("H")
print(f"Left stripped: {left_stripped}")

# Using maketrans(), partition(), replace(), rfind(), rindex(), rjust(), rpartition(), rsplt(), rstrip(), split(), splitlines(), startswith(), strip(), swapcase(), title(), translate(), upper(), zfill()
trans_table = str.maketrans("H", "J")
translated = sample_string.translate(trans_table)
print(f"Translated: {translated}")

partitioned = sample_string.partition("World")
print(f"Partitioned: {partitioned}")

replaced = sample_string.replace("World", "Universe")
print(f"Replaced: {replaced}")

r_find_hello = sample_string.rfind("World")
print(f"R-find 'World': {r_find_hello}")

r_index_hello = sample_string.rindex("World")
print(f"R-index 'World': {r_index_hello}")

right_justified = sample_string.rjust(50)
print(f"Right justified: {right_justified}")

r_partitioned = sample_string.rpartition("World")
print(f"R-partitioned: {r_partitioned}")

rsplitted = sample_string.rsplit(" ", 1)
print(f"RSplit: {rsplitted}")

rs_tripped = sample_string.rstrip(".")
print(f"R-strip: {rs_tripped}")

splitted = sample_string.split(" ")
print(f"Split: {splitted}")

split_lines = sample_string.splitlines()
print(f"Split lines: {split_lines}")

starts_with_hello = sample_string.startswith("Hello")
print(f"Starts with 'Hello': {starts_with_hello}")

stripped = sample_string.strip("!")
print(f"Strip: {stripped}")

swapped_case = sample_string.swapcase()
print(f"Swap case: {swapped_case}")

titled = sample_string.title()
print(f"Title: {titled}")

translated = sample_string.translate({ord('W'): ord('X')})
print(f"Translate: {translated}")

upper_cased = sample_string.upper()
print(f"Upper case: {upper_cased}")

zero_filled = sample_string.zfill(15)
print(f"Zero filled: {zero_filled}")
# String Methods using tetsing function():
s = "welcome to python"
print(s.isalnum())  #False
print("Welcome".isalpha())  #True
print("2012".isdigit())  #True
print("first Number".isidentifier())  #False
print(s.islower())  #True
print("WELCOME".isupper())  #True
print(" ".isspace())  #True

#Searching function
s = "welcome to python"
print(s.endswith("thon"))  #True
print(s.startswith("good"))  #False
print(s.find("come"))  #3
print(s.find("become"))  #-1
print(s.rfind("o"))  #15
print(s.count("o"))  #3

#converting Testing
s = "String in PYTHON"
s1 = s.capitalize()
print(s1)  #String in python
s2 = s.title()
print(s2)  #String In Python
s3 = s.lower()
print(s3)  #string in python
s4 = s.upper()
print(s4)  #STRING IN PYTHON
s5 = s.swapcase()
print(s5)  #sTRING IN python
s6 = s.replace("in", "on")
print(s6)  #String on PYTHON
print(s)  #String in PYTHON



