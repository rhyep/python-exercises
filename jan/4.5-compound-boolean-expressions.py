# 4.5-compound-boolean-expressions.py


'''
e 1     e 2     e 1 and e 2     e 1 or e 2      not e 1
False   False   False           False           True
False   True    False           True            True
True    False   False           True            False
True    True    True            True            False
'''

x = 10
y = 20

b = (x == 10)
print(b)

b = (x != 10)
print(b)

# and
b = (x == 10 and y == 20)
print(b)

b = (x != 10 and y == 20)
print(b)

b = (x == 10 and y != 20)
print(b)

b = (x != 10 and y != 20)
print(b)


# or
b = (x == 10 or y == 20)
print(b)

b = (x != 10 or y == 20)
print(b)

b = (x == 10 or y != 20)
print(b)

b = (x != 10 or y != 20)
print(b)


if x < 10 and input("Print value (y/n)?") == 'y':
    print(x)

if input("Print value (y/n)?") == 'y' and x < 10:
    print(x)

if x == 1 or 2 or 3:
    print("OK")

x == 1 or 2 or 3

(x == 1) or 2 or 3

if x == 1 or x == 2 or x == 3:
    print("OK")
