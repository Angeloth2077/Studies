def sort(array):
    
    for i in range(len(array)):
        
        index = i
        for j in range(i + 1, len(array)):
            
            if array[index] > array[j]:
                index = j
        
        array[i], array[index] = array[index], array[i]

array = []
a = 0
for i in range(0, 5):
    value = input("Enter a value: ")
    array.append(int(value))

print(array)
sort(array)
print(array)

