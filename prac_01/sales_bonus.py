"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter sales: $"))
while sales != 0:
    if sales > 1000:
        print("You got 15% bonus")
    elif sales > 0:
        print("You got 10% bonus")
    else:
        print("You have entered an invalid amount")
        exit(0)
    sales = float(input("Enter sales: $"))
print("Thank you for shopping with us")
