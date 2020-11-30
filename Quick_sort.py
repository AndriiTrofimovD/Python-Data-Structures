import random


def quick_sort(arr):
    """The function sorts and returns an array with the time complexity of O(log*n)"""
    if len(arr) < 2:
        return arr
    rand_index = random.randint(0, len(arr) - 1)
    pivot = arr[rand_index]
    arr2 = arr[:rand_index] + arr[rand_index + 1:]
    less = [i for i in arr2 if i < pivot]
    greater = [i for i in arr2 if i >= pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)
