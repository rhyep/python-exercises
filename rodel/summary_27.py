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
"""
from random import randrange


def sq(x):
    for i in range(x):
        for j in range(x):
            print("0",end="")
        print(end="\n")


def tr(x):

    for i in range(x+1):
        for j in range(i):
            print("0",end="")
        print(end="\n")

def rt(x):

    for i in range(x):
        for i in range(x):
            print("0",end="")
        x-=1
        print(end="\n")

def ra(x):

    for i in range(x):
        for i in range(randrange(1,x)):
            print("0",end="")
        print(end="\n")


def arr(x):
    for i in range(x):
        for j in range(i):
            if i<(x/2):
                print("0",end="")
        print("0")

"""
def fizzbuzz(x):

    for i in range(1,x+1):
        if i%3==0:
            print(i," = Fizz")
        elif i%5==0:
            print(i," = Buzz")
        elif  i%3==0 and i%5==0:
            print(i," = fizzbuzz")
        else:
            print(i," = FizzyBuzzy")






a=int(input("input sq: "))
fizzbuzz(a)