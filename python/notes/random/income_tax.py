income = int(input("Enter the income: "))

tax_payable = 0
if income <= 50000:
    tax_payable = income * 0.01

if income > 50000:
    if 2 < (income / 25000) <= 3:
        tax_payable = tax_payable + 500 + ((income-50000) * 0.02)
    else:
        tax_payable = tax_payable + 500 + (25000 * 0.02)
if income > 75000:
    if 3 < (income / 25000) <= 4:
        tax_payable = tax_payable + ((income - 75000) * 0.03)
    else:
        tax_payable = tax_payable + (25000 * 0.03)
if income > 100000:
    if 4 < (income / 25000) <= 10:
        tax_payable = tax_payable + ((income - 100000) * 0.04)
    else:
        tax_payable = tax_payable + (150000 * 0.04)
if income > 250000:
    tax_payable = tax_payable + ((income - 250000) * 0.05)


print("The tax payable would be $", format(tax_payable,'.1f'))

