def primeVerification(n):
    for i in range(1, n + 1):
        if i == 1 or i == n:
            continue
        if n % i != 0:
            return True
        if n % i == 0:
            return False

def run():
    n = int(input("Enter a number...\n"))

    if primeVerification(n) == True:
        print("Prime number")
    elif primeVerification(n) == False:
        print("No prime number")


if __name__ == '__main__':
    run()