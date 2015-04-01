# Data Input
tax_payer = input("Enter name of tax payer: ")
bldg_value = int(input("Enter assesed building value: "))
land_value = int(input("Enter assesed land value: "))
month = int(input("Enter month: "))

# Global Assignment Federation
basic_tax_bldg = bldg_value * 0.01
basic_tax_land = land_value * 0.01
total_annual_tax_land = basic_tax_land * 12
total_annual_tax_bldg = basic_tax_bldg * 12
discount_bldg = 0
discount_land = 0
total_discount = 0
penalty = 0
penalty_bldg = 0
penatly_land = 0
more_tax = 0
basic_tax = 0

# Condition
if land_value >= 50000:
    more_tax = land_value * 0.20

if month <= 3:
    discount_bldg = total_annual_tax_bldg * 0.20
    discount_land = total_annual_tax_land * 0.20
    total_discount = discount_bldg + discount_land
    total_annual_tax_bldg -= discount_bldg
    total_annual_tax_land -= discount_land
    print('Total Discount : %.2f' % (total_discount))
else:
    penalty_bldg = total_annual_tax_bldg * 0.20
    penalty_land = total_annual_tax_land * 0.20
    total_penalty = penalty_bldg + penalty_land
    total_annual_tax_bldg += penalty_bldg
    total_annual_tax_land += penalty_land
    print('Total Penalty : %.2f' % (total_penalty))

total_annual = total_annual_tax_land + total_annual_tax_bldg + more_tax
print('Total Annual : %.2f' % (total_annual))
