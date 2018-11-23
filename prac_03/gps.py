
import random

POPULATION = 1000


def main():
    print("Welcome to the Gopher Population Simulator")
    print("Starting population: ", POPULATION)
    year = 0

    while year <= 9:
        born_rate = random.randrange(10, 20)
        die_rate = random.randint(5, 25)
        born = POPULATION * born_rate // 100
        dead = POPULATION * die_rate // 100
        new_population = POPULATION + born - dead
        year += 1
        print("Year: ", year)
        print("********")
        print(born, "gophers were born.", dead, "died.")
        print("Population: ",  new_population)
        print("\n")
main()