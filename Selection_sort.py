
def selection_sort(arr):
    for i in range(len(arr)-1):
        index_of_min_value = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[index_of_min_value]:
                index_of_min_value = j
        arr[i], arr[index_of_min_value] = arr[index_of_min_value], arr[i]
    return arr

