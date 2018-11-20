char = input("Enter a character: ")
print("The ASCII code for {} is {}".format(char,ord(char)))
num = int(input("Enter a number between 33 and 127: "))
while num < 33 or num > 127:
    print("Invalid number")
    num = int(input("Enter a number between 33 and 127: "))
else:
    print("The character for {} is {}".format(num, chr(num)))
