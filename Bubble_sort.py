
def bubble_sort(arr):
    for i in range(len(arr)):
        done = True
        for j in range(1, len(arr) - i):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
                done = False
        if done:
            break
    return arr
