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

"""
def sq(x):
    for i in range(x):
        for j in range(x):
            print("0",end="")
        print(end="\n")

"""
"""
def tr(x):

    for i in range(x+1):
        for j in range(i):
            print("0",end="")
        print(end="\n")
"""

a=int(input("input sq: "))
tr(a)
