#summary10.py
"""
write a program that asks the user for his/her name ,age,
height in meters round off the height:
Sample output:
Enter name: jan
Enter age: 20
Enter height: 1.8
Jan\tis\t20\tyears\told\tand\tis\tapproximately\t20\tmeters\ttall.
"""
name = input("Enter name: ")
age = input("Enter age: ")
height = float(input("Enter height(meters): "))
print(name, "\tis\t", age, "\tyears\told\tand\tis\tapproximately\t",round(height),"\tmeters tall.")
