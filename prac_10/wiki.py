import wikipedia


def main():
    user_input = input("Please Enter your page title: ")
    while user_input != '':
        try:
            result = wikipedia.page(user_input)
            print(result.title)
            print(wikipedia.summary(result))
            print(result.url)
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)
        user_input = input("Please Enter your page title: ")
    print("Thank you for using our search engine")
    exit(0)


main()
