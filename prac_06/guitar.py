
from prac_06.guitars import Guitar

guitars = []

def main():
    choice = input("Would you like to enter your guitar detail? \nY/N: ").upper()
    while choice != "N":
        if choice == "Y":
            name = (input("Please enter your guitar name:\n>>> "))
            year = int(input("Please enter your guitar year:\n>>> "))
            cost = int(input("Please enter your guitar cost:\n>>> "))
            first_guitar = Guitar(name, year, cost)
            print(first_guitar)
    exit(0)

main()