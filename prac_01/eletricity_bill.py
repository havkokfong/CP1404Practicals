print("Electricity bill")
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

price = float(input("Please choose your tariff: 11 or 31: "))
if price == 11:
    price = TARIFF_11
elif price == 31:
    price = TARIFF_31
else:
    print("You have entered an invalid choice")
    price = float(input("Please choose your tariff: 11 or 31: "))
use = float(input("Enter daily use in kWh: "))
day = int(input("Enter number of billing days: "))
estimated = (price * use) * day
print("Estimated bill: {:.2f}".format(estimated))