import random as ran

def run():
    
    # Caracter lists
    aviableChars = [
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z'],
        ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z'],
        ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    ]

    # Initializing variables
    passwrd = []
    password = ''
    charts  = []

    # Adding all characters
    for list in aviableChars:
        for i in list:
            charts.append(i)

    # Password Generation Algorithm
    for char in range(15):
        random = ran.choice(charts)
        passwrd.append(random)

    password = ''.join(passwrd)
        
    # Output
    print("\nYour password is: " + password + "\n")


if __name__ == '__main__':
    run()