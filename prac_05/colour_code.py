""" Programming II colour code """

COLOUR = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "	#ffefdb", "AntiqueWhite2": "#eedfcc",
          "AntiqueWhite3": "#cdc0b0", "AntiqueWhite4": "#8b8378", "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6",
          "aquamarine4": "#458b740", "azure1": "#f0ffff", "azure2": "#e0eeee", "azure3": "#c1cdcd", "azure4": "#838b8b"}

MENU = ['AliceBlue', 'AntiqueWhite', 'AntiqueWhite', 'AntiqueWhite2', 'AntiqueWhite3', 'AntiqueWhite4', 'aquamarine1',
        'aquamarine2', 'aquamarine4', 'azure1', 'azure2', 'azure3', 'azure4']

def main():
    print("Welcome to colour code")
    for index, element in enumerate(MENU):
        print("{:<2}".format(index), "{:<15s}".format(element))
    print("\n")
    choice = input("Please select your colour: \n>>> ")
    for key, value in COLOUR.items():
        if choice in key:
            print("The code for ", key, "is", value)


main()
