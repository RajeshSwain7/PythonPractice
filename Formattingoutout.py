name, age, sal = "Rajesh", 26, 45000.96

# Approch-1 to print the name, age, sal
print(name, age, sal)

# Approch-2  of formatting the out put
print("Name is: ",name)
print("Age is: ",age)
print("Salary is: ",sal)

# Approch-3
# fromatting out put with the % & {}
# %d -> int
# %s -> String
# %f / %g -> float
print("Name:%s, Age:%d, salary:%g" % (name, age, sal))

# Approch-4
# using {}
print("Name:{}, Age:{}, salary:{}" .format(name, age, sal))