#List Operations
def move_elements():
    x = [1, 2, 3, 4, 5]
    y = []
    z = []

    while x:
        if len(z) < 3:
            z.append(x.pop(0))
        else:
            y.append(x.pop(0))
    y.reverse()
    print(f"x = {x}, y = {y}, z = {z}")

def insertion_sort_descending(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def selection_sort_ascending(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


#main
if __name__ == "__main__":
    move_elements()

    X = [1, 2, 21, 33, 45, 65, 12]
    sorted_desc = insertion_sort_descending(X.copy())
    sorted_asc = selection_sort_ascending(X.copy())

    print("Insertion Sort (Descending):", sorted_desc)
    print("Selection Sort (Ascending):", sorted_asc)



