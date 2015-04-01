# summary_20.py

""" Make a program that accepts name of a person ,monthly salary and should compute
    the withholding tax(withholding tax is 40% of his salary)
    If his net monthly salary is > 50000 print approves loan,otherwise not approves

expected output:
    Enter name:
    Enter salary:
    wTax:
    Loan:app or not apps
"""



name = input("Enter you name: ")
salary = float(input("Enter your salary:"))
wTax = salary * .40

print("NAME:",name,"\n","SALARY:",salary,"\n","WTAX:",wTax,"\n","NET:",salary-wTax,"\n","LOAN:","Approve loan" if salary>50000  else  "Not approve")
#print ()
