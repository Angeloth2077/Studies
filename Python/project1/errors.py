def run():

    palindrome = lambda string: string == string[::-1]
    string = input("\nEnter a string: ")
    
    try:
        print(palindrome(string))
    except TypeError:

        print("Please enter a string not a number")


if __name__ == '__main__':
    run()