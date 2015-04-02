# summary_20_2.py

"""
Write a program that accepts the name of a tax payer, accepts
 the current assessed value of the building
and land,
compute the  basic tax by
1 percent  of assessed value of both building and land

compute the annual basic tax of both building and land
compute the total annual tax

if the assessed value  of the land
greater than or equal to 50,000 compute additional
 tax of 20 percent of his land assessed value

accepts the current month in integer. if current month is march (3)
 and below compute for the discount (20 percent of
annual basic tax of building and land) else compute for the penalty
(20 percent of annual  tax value of building and land).

"""


payerName = input("Enter Name: ")
assessedValueBuilding = float(input("Enter assessed value(building): "))
assessedValueLand = float(input("Enter assessed value(land): "))
month = int(input("Enter month:"))

discLand = 0
discBuilding = 0

penaltyLand = 0
penaltyBuilding = 0

additionalTax = 0

taxLand = .01 * assessedValueLand
taxBuilding = .01 * assessedValueBuilding

landAnnualTax = taxLand * 12
buildAnnualTax = taxBuilding * 12


if(assessedValueLand >= 50000):
    additionalTax = .20 * assessedValueLand


if(month <= 3):
    discLand = .20 * landAnnualTax
    discBuilding = .20 * buildAnnualTax
    landAnnualTax -= discLand
    buildAnnualTax -= discBuilding

else:
    penaltyLand = .20 * landAnnualTax
    penaltyBuilding = .20 * buildAnnualTax
    landAnnualTax += penaltyLand
    buildAnnualTax += penaltyBuilding


totalAnnual = landAnnualTax + buildAnnualTax + additionalTax
totalDisc = discLand + discBuilding
totalPenalty = penaltyLand + penaltyBuilding


print(
    "NAME:",
    payerName,
    "\nBUILDING>>",
    "\nDISCOUNT:",
    "%.2f" %
    discBuilding,
    "\nPENALTY:",
    "%.2f" %
    penaltyBuilding,
    "\nTOTAL ANNUAL TAX:",
    "%.2f" %
    buildAnnualTax,
    "\nLAND>>",
    "\nDISCOUNT:",
    "%.2f" %
    discLand,
    "\nPENALTY:",
    "%.2f" %
    penaltyLand,
    "\nTOTAL ANNUAL TAX:",
    "%.2f" %
    landAnnualTax,
    "\n\n",
    "\nTOTAL ANNUAL TAX:",
    "%.2f" %
    totalAnnual,
    "\n TOTAL DISC:",
    "%.2f" %
    totalDisc,
    "\nPENALTY:",
    "%.2f" %
    totalPenalty)
