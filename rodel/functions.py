# functions.py

from math import sqrt
from random import randrange, seed
x = sqrt(16)
print(x)

y = 2 * sqrt(x + 16) - 4
print(y)

seed(23)
for i in range(0, 101):
    print(randrange(1, 1001))

# writing functions
# 1st kind of function


def nameoffunc():
    print("I am a function")

nameoffunc()

# 2nd type of functin


def nameoffunc2(name, lastname):
    print("I am ", name, lastname)

nameoffunc2("Rodel", "Rebucas")

# function 3

a = 4 b = 1


def func3():
    c = a + b
    return c

print(func3())

# function 4


a = 1


def func4(a):
    c = a + 5
    return c

print(func4(a))
