"""
Write a program that asks the user for
his/her name, age, height in meters.
Round of the height
"""

name = input("Enter name: ")
age = input("Enter age: ")
height = float(input("Enter height: "))
r_height = round(height)

print(name, '\tis\t', age, 'year\'s old\t')
print('and\tis\tapproximately\t', r_height, 'meter\'s tall')
