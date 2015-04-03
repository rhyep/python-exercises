# summary_27.py

"""
a=3
sq(x)
000
000
000
sq(a)


tr(x)
0
00
000
tr(a)

rt(x)
000
00
0
rt(a)

ra(x)
00
000
0
ra(a)

arr(x)

calls sq function when x is lesser than
or equak to 5 else display:
0
00
000
0
0
0

"""

from random import randrange


def sq(x):
    for i in range(x):
        print("0" * x, end="")
        print()

def tr(x):
    for i in range(x + 1):
        for j in range(i):
            print("0", end="")
        print("")


def rt(x):
    for i in range(x):
        for i in range(x):
            print("0", end="")
        x -= 1
        print("")


def ra(x):
    for i in range(x):
        for i in range(randrange(1, x)):
            print("0", end="")
        print("")


def arr(x):
    if x > 5:
        for i in range(x):
            for j in range(i):
                if i < (x / 2):
                    print("0", end="")
            print("0")
    else:
        sq(x)


def fizzbuzz(x):
    for i in range(1, x + 1):
        if i % 3 == 0:
            print(i, " = Fizz")
        elif i % 5 == 0:
            print(i, " = Buzz")
        elif i % 3 == 0 and i % 5 == 0:
            print(i, " = fizzbuzz")
        else:
            print(i, " = FizzyBuzzy")


cont = "y"

while cont == "y":
    a = int(input("input sq:"))
    sq(a)
    tr(a)
    rt(a)
    ra(a)
    arr(a)
    fizzbuzz(a)
    cont = input("Do you want to continue?y/n: ")
