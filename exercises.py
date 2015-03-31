# Comments

# This is a single line comment.
"""
This is a multiple line comment.
This is a multiple line comment.
This is a multiple line comment.
"""


# Values and Variables
print("I am a string") 	# String
string = "String 2"
print(string)
print(7)				# Integer
y = 2 					# assignment
print(y) 				# variable

# valid identifiers
x2 = 1
total = 3
port_80 = 80

# Float
f = 21.21

# type
type(4)
f = 20.1
type(f)
type("Hey!")

# multiple assignment
a = 20
a = 30
a = 40

# round
a = 2.1
b = round(a)
a = 2.6
c = round(a)
aa = 2.15254
b = round(aa, 3)


# string control codes
print("A\nB\nC")
print("D\tE\tF")


# escape quotes
print("'single'")
print('"double"')
print('\'singlescape\'')
print("\"doublescape\"")


# user input
print("Enter integer: ")
i = input()
print("You've entered ", i)
print("Type: ", type(i))
x = input("Enter value of x")
print(x)


# print function
print("end with end", end="")
print("end with newline", end="\n")

x, y, z = 1, 2, 3
print(x, y, z)
print(x, y, z, sep="-")

print('{0} {1}'.format(0, 10 ** 0))
print('{0} {1}'.format(1, 10 ** 1))
print('{0} {1}'.format(2, 10 ** 2))
print('{0} {1}'.format(3, 10 ** 3))
print('{0} {1}'.format(4, 10 ** 4))


# arithmetic expressions
a = 1
b = 2
c = a + b
d = a - b
e = a * b
f = a / b
g = a // b
h = a % b
i = a ** b

# mix type
a = 10
b = 2.2
c = a + b

# precedence
d = (c + a) * b
e = c + a * b

# other
x = 1
y = 2
x += y
x +- y

# conditinal and boolean expressions
True
False
type(True)
type(False)

a = 1
b = 2

# if statement
if a > 1:
	print("a is >")
if a == 1:
	print("a == 1")
if a <= 1:
	print("a == 1")
if a < 1:
	print("a < 1")

# else
if a == 1:
	print("a == 1")
else:
	print("a != 1")

# compound boolean
if a == b and b == 0:
	print("a = b, b = 0")
if a == b or b == 0:
	print("or")
if a == b not b == 0:
	print("not b = 0")


# pass
a = 10
b = 20
if a > b:
	pass # do nothing
else:
	print("else")


# elif
a = "a"
if a == "x":
	print("x")
elif a == "y":
	print("y")
elif a == "a":
	print("a")
else:
	print("dunno")


# Iteration
print(1)
print(2)
print(3)

# while loop
count = 1
while count <= 3:
	print(count)
	count += 1

# for loop
for n in range(1, 101):
	print(n)
for n in range(100):
	print(n)

# for step
for n in range(100, 0, -5):
	print(n)

# nested loops
for r in range(11):
	for c in range(11):
		p = r * c
		print(p, end=" ")
	print()

# function
x = 16
print(sqrt(16.0))
y = 2 * sqrt(x + 16) - 4
print(y)

# random
from random import randrange, seed
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
