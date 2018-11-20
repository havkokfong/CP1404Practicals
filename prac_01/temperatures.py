"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""

def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            fahrenheit = cal_celsius()
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            celsius = cal_fahrenheit()
            print("Result: {:.2f} C".format(celsius))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def cal_fahrenheit():
    fahrenheit = float(input("Fahrenheit: "))
    celsius = 5 / 9.0 * (fahrenheit - 32)
    return celsius


def cal_celsius():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


main()