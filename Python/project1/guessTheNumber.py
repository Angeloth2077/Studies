import random

guess = 0
number = random.randint(0, 10)


def ask(g):
    g = int(input("Your guess...\n"))    
    return g 

def game(g):
    while g != number:
        if g < number:
            print("The number is higher")
            g = ask(g) 
        elif g > number:
            print("The number is lower")
            g = ask(g) 
    return g
def won():
    print("Congratulations you guessed right!")


def run():

    ask(guess)
    game(guess)
    won()



if __name__ == '__main__':
    run()