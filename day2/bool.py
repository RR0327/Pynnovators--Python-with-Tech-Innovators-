#Booleans represent one of two values: True or False.

print(10 > 9)
print(10 == 9)
print(10 < 9)

#The bool() function allows you to evaluate any value, and give you True or False in return,

print(bool(" "))
print(bool(0))

print(bool(()))

#Python also has many built-in functions that return a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type:
x = 200
print(isinstance(x, int))