# 1 This is a single line comment.
"""
This is a multiple line comment.
This is a multiple line comment.
This is a multiple line comment.
"""


# 2 values and variable
print("I am a string")     # String
string = "String 2"
print(string)
print(7)                # Integer
y = 2                     # assignment
print(y)                 # variable


# 3 valid identifiers
x2 = 1
total = 3
port_80 = 80


# 4 float
f = 21.21
ff = 21.212121
print("%.2f" % f)
print("%.3f" % ff)


# 5 type
print(type(4))
f = 20.1
print(type(f))
print(type("Hey!"))


# 6 multiple assignment
a = 20
a = 30
a = 40
print(a)
a, b, c = 10, 20, 30
print(a, b, c)


# 7 round
a = 2.1
b = round(a)
print(a)
a = 2.6
c = round(a)
print(c)
aa = 2.15254
print(aa)
b = round(aa, 3)
print(b)


# 8 string control codes
print("A\nB\nC")
print("D\tE\tF")


# 9 escape quotes
print("'single'")
print('"double"')
print('\'singlescape\'')
print("\"doublescape\"")


# 10 user input
print("Enter integer: ")
i = input()
print("You've entered ", i)
print("Type: ", type(i))
x = input("Enter value of x")
print(x)


# 11 print function
print("end with end", end="")
print("end with newline", end="\n")
print("end with nothing", end="")
print("end with tab", end="\t")

x, y, z = 1, 2, 3
print(x, y, z)
print(x, y, z, sep="-")

print('{0} {1}'.format(0, 10 ** 0))
print('{0} {1}'.format(1, 10 ** 1))
print('{0} {0}'.format(2, 10 ** 2))
print('{1} {1}'.format(3, 10 ** 3))
print('{0} {1}'.format(4, 10 ** 4))
print('{1} {1}'.format(4, 4))


# 12 arithmetic expressions
a = 1
b = 2
c = a + b
d = a - b
e = a * b
f = a / b
g = a // b  # floor division
h = a % b
i = a ** b
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)


# 13 mix type
a = 10
b = 2.2
c = a + b
print(c)


# 14 precedence
a = 1
b = 2
c = 3
d = (c + a) * b
e = c + a * b
f = a + a * b + c
h = a + b**b + (a + b)


# 15 compound operators
x = 1
y = 2
x += y
y -= x
print(x, y)


# 16 boolean expressions
print(True)
print(False)
print(type(True))
print(type(False))


# 17 if statement
a = 1
b = 2

if a > 1:
    print("a is >")
if a == 1:
    print("a == 1")
if b <= 1:
    print("b <= 1")
if b < 1:
    print("b < 1")


# 18 else
if a == 1:
    print("a == 1")
else:
    print("a != 1")


# 19 compound boolean, operators
a = 1
b = 2

if a == b and b == 0:
    print("a = b, b = 0")
else:
    print("and!")
if a == b or b == 2:
    print("or!")

if a == b or not b == 2:
    print("or!")


# 20 pass
a = 10
b = 20
if a > b:
    pass  # do nothing
else:
    print("else")

if a < b:
    pass  # do nothing
else:
    print("else")


#  21 elif
a = "a"
if a == "x":
    print("x")
elif a == "y":
    print("y")
elif a == "a":
    print("a")
else:
    print("dunno")


# 22 nested if else
name = "jan"
if "j" in name:
    if "a" in name:
        print("yay!")
    else:
        print("non")
    if "n" in name:
        print("letters")
else:
    print("non")


# 23 Iteration
print(1)
print(2)
print(3)
a = 0
print(a + 1)
print(a + 1)
print(a + 1)


# 24 while loop
count = 1
while count <= 3:
    print(count)
    count += 1


# 25 for loop
for n in range(1, 101):
    print(n)

for n in range(100):
    print(n)

for n in range(100, 0, -5):
    print(n)


# 26 nested loops
for r in range(11):
    for c in range(11):
        p = r * c
        print(p, end=" ")
    print()


# 27 function
# from math import sqrt
x = 16
print(sqrt(16.0))
y = 2 * sqrt(x + 16) - 4
print(y)


# random
# from random import randrange, seed
seed(23)
for i in range(0, 100):
    print(randrange(1, 1001), end=" ")


# writing functions
def count(n):
    for i in range(n + 1):
        print(i)

count(10)


# lambda
def evaluate(f, x, y):
    return f(x, y)

evaluate(lambda x, y: 3*x + y, 10, 2)


# generators
def remember():
    global count
    count += 1
    print(str(count))

remember()
remember()


def gen():
    yield 3
    yield "wow"
    yield 1.3
    yield -4

print(gen)
print(type(gen))
print(gen())
x = x gen()
print(x)
print(next(x))
print(next(x))


# objects
s = "ABCDEFG"
print(len(s))
print(s[2])


# file objects
file = open('file.txt', 'r')
for line in file:
    print(line)


# fraction
frac = Fraction(1, 3)
print(frac)
print(frac.numerator)
print(frac.denominator)


# list
a = []
a.append(1, "a", 1.2)
print(a)
a[2]

for i in a:
    print(i)

a[:2]
a[-1:]


# list comprehension
b = [x ** 2 for x in range(20)]
