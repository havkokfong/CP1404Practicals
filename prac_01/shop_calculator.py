print("Welcome to shop calculator")
DISCOUNT = 0.9
num = int(input("Please enter the number of item: "))
while num <= 0:
    print("You have entered an invalid number")
    num = int(input("Please enter the number of item: "))
total = 0.0
for i in range (0, num):
    price = float(input("Please enter price of the item: "))
    total += price
    print("price= $", price,"Total= $", total)
    if total <= 100:
        total = DISCOUNT * total
print("Number of item: ", num)
print("Total= $", total)
