""" Make a program that accepts name of person
that accepts monthly salary, it should compute
 for his withholding tax. Withholding tax is
 equals to 40 percent of his salary.
 If his net monthly salary is greater than
 50,000. Put \'"approved loan\" else output not approved.
 """
name = input("Enter name: ")
print("Hi,", name.capitalize())
salary = int(input("Please enter salary: "))
w_tax = 0.40
overall = salary - (salary * w_tax)

if salary >= 50000:
    print("Approved Loan")
if salary < 50000:
    print("Loan not granted")
print('Gross Salary: %.2f' % (salary))
print('Net Salary: %.2f' % (overall))
print('Witholding tax: ', salary * w_tax)
