

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = i
        while key > 0 and arr[key-1] > arr[key]:
            arr[key-1], arr[key] = arr[key], arr[key-1]
            key -= 1
    return arr
