

from prac_06.programming_language import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(ruby)
    print(python)
    print(visual_basic)
    store = [ruby, python, visual_basic]
    print("\nThe Dynamically typed language are: ")
    for i in store:
        if i.is_dynamic() is True:
            print(i.name)


main()
