import random



def main():
    ranges = int(input("How many quick picks?\n>>> "))
    for j in range(1, ranges + 1):
        for i in range(5):
            numbers = random.randint(1, 45)
        if i in numbers:
            numbers = random.randint(1, 45)
    print(numbers, end=" ")


main()