# 3.1-expressions.py

value1 = eval(input('Please enter a number: '))
value2 = eval(input('Please enter another number: '))
sum = value1 + value2
print(value1, '+', value2, '=', sum)

'''
x + y   x added to y, if x and y are numbers
        x concatenated to y, if x and y are strings
x - y   x take away y, if x and y are numbers
x * y   x times y, if x and y are numbers
        x concatenated with itself y times,
            if x is a string and y is an integer
        y concatenated with itself x times,
            if y is a string and x is an integer
x / y   x divided by y, if x and y are numbers
x // y  Floor of x divided by y, if x and y are numbers
x % y   Remainder of x divided by y, if x and y are numbers
x ** y  x raised to y power, if x and y are numbers
'''

x, y, z = 3, -4, 0
x = -x
y = -y
z = -z
print(x, y, z)

one = 1.0
one_third = 1.0/3.0
zero = one - one_third - one_third - one_third
print('one =', one, ' one_third =', one_third, ' zero =', zero)

one = 1.0
one_tenth = 1.0/10.0
zero = one - one_tenth - one_tenth - one_tenth \
            - one_tenth - one_tenth - one_tenth \
            - one_tenth - one_tenth - one_tenth \
            - one_tenth
print('one =', one, ' one_tenth =', one_tenth, ' zero =', zero)

one = 1.0
one_fourth = 1.0/4.0
zero = one - one_fourth - one_fourth - one_fourth - one_fourth
print('one =', one, ' one-fourth =', one_fourth, ' zero =', zero)
