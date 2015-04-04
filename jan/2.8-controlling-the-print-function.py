# 2.8-controlling-the-print-function.py

# end with no new line '\n'
print('Please enter an integer value:', end='')
print(end='Please enter an integer value: ')

# ends with a new line, also a default
print('Please enter an integer value:')
print('Please enter an integer value:', end='\n')

# the same
print()
print(end='\n')

print('A', end='')
print('B', end='')
print('C', end='')
print()
print('X')
print('Y')
print('Z')

# separator
w, x, y, z = 10, 15, 20, 25
print(w, x, y, z)
print(w, x, y, z, sep=',')
print(w, x, y, z, sep='')
print(w, x, y, z, sep=':')
print(w, x, y, z, sep='----')
