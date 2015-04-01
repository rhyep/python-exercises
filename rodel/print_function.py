#print_function.py

print("end with end", end=" ")
print("end with end", end="\n")
print("end with end", end="")
print("end with end", end="\t")
x, y, z = 1, 2, 3
print(x, y, z)
print(x, y, z, sep="-")

print('{0} {1}'.format(0, 10**0))
print('{0} {1}'.format(1, 10**1))
print('{0} {1}'.format(2, 10**2))
print('{0} {1}'.format(2, 10**3))
print('{1} {1}'.format(100, 200))
