# summary_20_2.py

"""
Write a program that accepts the name of a tax payer,
"""
name = input("Tax Payer : ")

"""
accepts the current assessed value of the building and land,
"""
print("\nAssessed value")
assessed_value_bldg = float(input("Building : "))
assessed_value_land = float(input("Land : "))

"""
compute the basic tax by 1 percent of the assessed value both building and land
then compute both it's annual tax
then compute the total annual tax
"""

annual_basic_tax_land = (assessed_value_land * .01) * 12
annual_basic_tax_bldg = (assessed_value_bldg * .01) * 12

total_annual_tax = annual_basic_tax_land + annual_basic_tax_bldg


"""
if the assessed value of the land is greater than or equal to 50,000
    compute additional tax of 20 percent of his land assessed value.
"""


"""
accepts the current month in integer.
"""
month = int(input("\n\nEnter month in integer : "))


"""
if current month is march (3) and  below or before
compute for the discount
    (20 percent of annual_basic_tax both building and land)
else
    compute for the penalty
    (20 percent of annual_basic_tax both building and land).
"""

if month <= 3:
    discount_land = annual_basic_tax_land * .20
    discount_bldg = annual_basic_tax_bldg * .20

    total_discount = discount_land + discount_bldg

    annual_land_tax = annual_basic_tax_land - discount_land
    annual_bldg_tax = annual_basic_tax_bldg - discount_bldg

    total_annual_tax = annual_land_tax + annual_bldg_tax

    penalty_land = 0
    penalty_bldg = 0
    total_penalty = 0

else:
    penalty_land = annual_basic_tax_land * .20
    penalty_bldg = annual_basic_tax_bldg * .20

    total_penalty = penalty_land + penalty_bldg

    annual_land_tax = annual_basic_tax_land + penalty_land
    annual_bldg_tax = annual_basic_tax_bldg + penalty_bldg

    total_annual_tax = annual_land_tax + annual_bldg_tax

    discount_land = 0
    discount_bldg = 0
    total_discount = 0


if assessed_value_land >= 50000:
    additional_tax = assessed_value_land * .2
    total_annual_tax += additional_tax
else:
    additional_tax = 0


print("\nAdditional tax : %.2f\n" % additional_tax)

print("Total")
print("Annual tax : %.2f" % total_annual_tax)
print("Discount : %.2f" % total_discount)
print("Penalty : %.2f" % total_penalty)

print()

print("Building")
print("Annual tax : %.2f" % annual_bldg_tax)
print("Discount : %.2f" % discount_bldg)
print("Penalty : %.2f" % penalty_bldg)

print()

print("Land")
print("Annual tax : %.2f" % annual_land_tax)
print("Discount : %.2f" % discount_land)
print("Penalty : %.2f" % penalty_land)
