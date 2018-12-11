
from prac_06.guitars import Guitar


def main():
    first_guitar = Guitar("Gibson L -5", 1922, 0)
    print(first_guitar.get_age())
    print(first_guitar.is_vintage())
main()