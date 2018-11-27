import random



def main():
    range = int(input("How many quick picks?"))
    for i in range(1, range + 1):
        numbers = random.randint(1, 45)
        print(numbers)

main()