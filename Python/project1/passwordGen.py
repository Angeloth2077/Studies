import random as ran

def run():
    
    # Caracter lists
    MAYUS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    MINUS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    # Adding all characters
    aviableChars = MAYUS + MINUS + NUMS

    # Initializing variables
    passwrd = []
    password = ''
    # Password Generation Algorithm
    for char in range(15):
        random = ran.choice(aviableChars)
        passwrd.append(random)

    password = ''.join(passwrd)
        
    # Output
    print("Your password is: " + password)


if __name__ == '__main__':
    run()