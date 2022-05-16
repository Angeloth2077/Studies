def sort(num):
    n = len(num)
    for i in range(n):
        for j in range(0, n - i - 1):
            if num[j] > num[j+1]:
                 num[j], num[j+1] = num[j+1], num[j]
    return num
array = [23, 43, 2, 11, 2, 5]
print(array)
x = sort(array)
print(x)
