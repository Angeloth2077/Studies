def sort(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

array = []
a = 0
for i in range(0, 5):
    value = input("Enter a value: ")
    array.append(int(value))

print(array)
sort(array)
print(array)

