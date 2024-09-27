#insertion sort
arr1 = [10, 3, 2, 1, 1, 4, 89, 21]
print("arr1 before Insertion Sort:", arr1)
for i in range(1, len(arr1)):
    key = arr1[i]
    j = i - 1
    #move elements of arr1[0...i-1] that are greater than the key to one position ahead of their current position
    while j >= 0 and key < arr1[j]: #change the conditions for ascending and descending
        arr1[j + 1] = arr1[j]
        j -= 1
    arr1[j + 1] = key
print("arr1 after Insertion Sort:", arr1)
print()
#selection sort
arr2 = [10, 2, 3, 1, 1, 4, 89, 21]
print("arr2 before Selection Sort:", arr2)
for i in range(len(arr2)):
    min_idx = i
    for j in range(i + 1, len(arr2)):
        if arr2[min_idx] > arr2[j]:
            min_idx = j
    arr2[i], arr2[min_idx] = arr2[min_idx], arr2[i]
print("arr2 after Selection Sort:", arr2)
print()
#bubble sort
arr3 = [10, 2, 3, 1, 1, 4, 89, 21]
print("arr3 values before Bubble Sort:", arr3)
for i in range(len(arr3)):
    for j in range(0, len(arr3) - i - 1):
        if arr3[j] > arr3[j + 1]:
            arr3[j], arr3[j + 1] = arr3[j + 1], arr3[j]
print("arr3 after Bubble Sort:", arr3)
print()

