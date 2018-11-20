MENU = """(E) Show the even numbers from x to y
(O) Show the odd numbers from x to y
(S) Show the squares from x to y
(Q) Exit the program"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "E":
        print("Show the even number from x to y")
    elif choice == "O":
        print("Show the odd number from x to y")
    elif choice == "S":
        print("Show the squares from x to y")
    else:
        print("You have entered an invalid letter")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you")