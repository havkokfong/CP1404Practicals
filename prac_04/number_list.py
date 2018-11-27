""" Practical_4 Part 2"""

def main():
    numbers = []
    number = 5
    for number in range(1, number + 1):
        number = int(input("Please enter " + str(number) + " number: "))
        numbers.append(number)
    print("The first numbers is: " + str(numbers[0]))
    print("The last number is: " + str(numbers[-1]))
    print("The smallest number is: " + str(min(numbers)))
    print("The largest number is: " + str(max(numbers)))
    average = sum(numbers)/len(numbers)
    print("The average of the numbers is: ", average)
main()
