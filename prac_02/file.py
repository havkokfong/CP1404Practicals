out_file = open("name.txt", "w")
name = input("What is your name? \n: ")
print(name, file = out_file)
out_file.close()

in_file = open("name.txt", "r")
name = in_file.read(). strip()
print("Your name is", name)
in_file.close()

num_file = open("numbers", "r")
number1 = int(num_file.readline())
number2 = int(num_file.readline())
print(number1 + number2)
num_file.close()


in_file = open("numbers", "r")
total = 0
for line in in_file:
    number = int(line)
    total += number
print(total)
in_file.close()