from random import randrange, seed


def sq(x):
    for n in range(x):
        print('0' * x)


def tr(x):
    for n in range(x + 1):
        print('0' * n)


def rt(x):
    for n in range(x, 0, -1):
        print('0' * n)


def ra(x):
    for n in range(x):
        print('0' * randrange(1, x + 1))


def arr(x):
    if x <= 5:
        sq(a)
    else:
        for n in range(x + 1):
            if n <= x / 2:
                print('0' * n)
            else:
                print('0')

# FIZZBUZZ


def fizzbuzz(x):
    for x in range(1, x + 1):
        print(x, end="")
        if x % 3 == 0 and x % 5 != 0:
            print(" fizz")
        if x % 5 == 0 and x % 3 != 0:
            print(" buzz")
        if x % 3 == 0 and x % 5 == 0:
            print(" fizzbuzz")
        if x % 3 != 0 and x % 5 != 0:
            print(" fizzbuzzy")

terminate = 'y'
while terminate == 'y':
    a = int(input("Enter input: "))
    sq(a)
    tr(a)
    rt(a)
    ra(a)
    arr(a)
    fizzbuzz(a)
    terminate = (input('Do you want to continue: y/n '))
