# Databricks notebook source
print("Hello Eshan!")

# COMMAND ----------

if 5 > 2:
  print("Five is greater than two!")

# COMMAND ----------

if 5 > 2:
 print("Five is greater than two!")
 print("Five is greater than two!")

# COMMAND ----------

x = 5
y = "Hello, World!"
x = "new value"
print(x)
print(y)


# COMMAND ----------


print("Hello, World!") #This is a comment

# COMMAND ----------

#This is a comment
#written in
#more than just one line
print("Hello, World!")

# COMMAND ----------

"""
This is a comment
written in
more than just one line
"""

print("Hello, World!")

# COMMAND ----------

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))



# COMMAND ----------

#x = "John"
# is the same as
x = 'John'

print(x)

# COMMAND ----------

_a = 4
_A = "Sally"
#A will not overwrite a

print(_a)
print(_A)

# COMMAND ----------

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# COMMAND ----------

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# COMMAND ----------

x = y = z = "Orange"
print(x)
print(y)
print(z)

# COMMAND ----------

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
print(fruits)

# COMMAND ----------

x = "awesome"
print("Python is " + x)

# COMMAND ----------

x = "Python is "
y = "awesome"
z =  x + y
print(z)

# COMMAND ----------

x = 5
y = 10
print("Sum: " + str(x))

# COMMAND ----------

x = 5
y = "John"
print(str(x) + y)

# COMMAND ----------

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

# COMMAND ----------

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

# COMMAND ----------

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

# COMMAND ----------

x = "awesome"

def myfunc():
  global x 
  x = "sgfsfesfantastic"

myfunc()

print("Python is " + x)

# COMMAND ----------

x = True
print(type(x))
print(x)

# COMMAND ----------

x = 3+5j
y = 12E4
z = -87.7e100

print(x)
print(type(y))
print(z)

# COMMAND ----------

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# COMMAND ----------

import random

print(random.randrange(1, 1064353454))

# COMMAND ----------
# COMMAND ----------
# COMMAND ----------
# COMMAND ----------
