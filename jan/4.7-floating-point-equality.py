# 4.7-floating-point-equality.py


d1 = 1.11 - 1.10
d2 = 2.11 - 2.10

print('d1 =', d1, ' d2 =', d2)

if d1 == d2:
    print('Same')
else:
    print('Different')

d1 = 0.010000000000000009
d2 = 0.009999999999999787
print(d1 == d2)


d1 = 1.11 - 1.10
d2 = 2.11 - 2.10

print('d1 =', d1, ' d2 =', d2)

diff = d1 - d2  # Compute difference
if diff < 0:  # Compute absolute value
    diff = -diff
if diff < 0.0000001:  # Are the values close enough?
    print('Same')
else:
    print('Different')


d1 = 1.11 - 1.10
d2 = 2.11 - 2.10

print('d1 =', d1, ' d2 =', d2)

if -0.0000001 < d1 - d2 < 0.0000001:
    print('Same')
else:
    print('Different')
