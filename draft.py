# def my_function(fname = "hello"):
#   print(fname + " Refsnes")

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")
# my_function()

#######################################

# def my_function(**kid):
#   print("His last name is " + kid["lname"])

# my_function(fname = "Tobias", lname = "Refsnes") 

#############################################


# def my_function(food):
#   for x in food:
#     print(x)

# fruits = ["apple", "banana", "cherry"]

# my_function(fruits)

# fruits = ("A", "B", "C")
# my_function(fruits)

#############################################

# x = 123
# def myFunc():
#     x = 10
#     print(id(x))

# myFunc()
# print(id(x))

# def myFunc2():
#     global x
#     x = 100
#     print(id(x))
# myFunc2()
# print(id(x))

##############################
# import inc.utils

# print(inc.utils.sub(5,8))

##############################

# import platform

# print(platform.system())

###############################
# import importlib
# print(importlib.import_module("os"))

################################

lis =  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(lis)
print(lis[:])
print(lis[1:])
print(lis[1::])
print(lis[:1])
print(lis[1:5])
print(lis[0::6])

print ('\n\n')
lis =  (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

print(lis)
print(lis[:])
print(lis[1:])
print(lis[1::])
print(lis[:1])
print(lis[1:5])
print(lis[0::6])