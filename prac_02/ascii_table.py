
def main():

    char = input("Enter a character: ")
    while char > 1:
        print("Invalid letter")
        char = input("Enter a character: ")
    print("The ASCII code for {} is {}".format(char,ord(char)))
    get_number()


def get_number():
    num = int(input("Enter a number between 33 and 127: "))
    while num < 33 or num > 127:
        print("Invalid number")
        num = int(input("Enter a number between 33 and 127: "))
    else:
        print("The character for {} is {}".format(num, chr(num)))


main()