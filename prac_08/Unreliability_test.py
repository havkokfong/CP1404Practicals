
from prac_08.unreliable_car import UnreliableCar
import random


RELIABILTY = random.uniform(0, 100)


def main():
    testing = UnreliableCar("Toyota", 150, RELIABILTY)
    testing.drive(50)
    print(testing)

main()
