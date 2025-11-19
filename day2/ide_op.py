#The is operator returns True if both variables point to the same object:
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

print(x is not y)