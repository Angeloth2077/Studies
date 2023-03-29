def run():

    full = [i for i in range(1, 51)]

    even = list(filter(lambda x : x % 2 == 0, full))
    odd = list(filter(lambda x: x % 2 != 0, full))

    print(even)
    print(odd)


if __name__ == '__main__':
    run()