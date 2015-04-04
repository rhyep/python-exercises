from random import randrange

'''
a = 3
sq(x)
OOO
OOO
OOO
sq(a)
'''


def sq(x):
    for n in range(x):
        print('O' * x)


'''
a = 3
tr(x)
O
OO
OOO
tr(a)
'''


def tr(x):
    for n in range(1, x + 1):
        print('O' * n)


'''
a = 3
rt(x)
OOO
OO
O
rt(a)
'''


def rt(x):
    for n in range(x, 0, -1):
        print('O' * n)


'''
a = 3
(random)
ra(x)
OOO
O
OO
ra(a)
'''


def ra(x):
    for n in range(x):
        print('O' * randrange(1, x + 1))


'''
arr(x)
x <= 5
sq(a)
x >= 6
O
OO
OOO
O
O
O
arr(a)
'''


def arr(x):
    for n in range(1, x + 1):
        if(n <= x / 2):
            print('O' * n)
        else:
            print('O')


def fizzbuzz(x):
    for n in range(1, x + 1):
        word = ''
        if n % 3 == 0:
            word += 'fizz'
        if n % 5 == 0:
            word += 'buzz'
        if(n % 3 != 0 and n % 5 != 0):
            word += 'fizzybuzzy'
        print(n, word)


choice = 'y'
while choice == 'y':
    a = int(input('Positive integer  : '))
    sq(a)
    print()
    tr(a)
    print()
    rt(a)
    print()
    ra(a)
    print()
    arr(a)
    print()
    fizzbuzz(a)
    choice = input('Continue? (y/n): ')
