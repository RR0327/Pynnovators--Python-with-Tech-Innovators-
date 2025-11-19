def my_function(temp2):
    celsius2 = (temp2 - 32) * 5 / 9
    return celsius2
print(my_function(100))
print(my_function(50))
print(my_function(75))

def my_function(*, name):
  print("Hello", name)

my_function("Emil")