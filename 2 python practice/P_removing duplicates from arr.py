
import numpy as np


def remove_duplicates(arr):
    new_arr = np.array([])

    for i in arr:
        if i not in new_arr:
            new_arr = np.append(new_arr, i)

    return np.sort(new_arr)


def remove_duplicates2(arr):
    i=0
    while i < len(arr):
        if arr[i] in arr[i+1:]:
            arr = np.delete(arr, i)
        else:
            i += 1
    return arr

# optimized way
def remove_duplicates3(arr):
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] in arr[:i]:
            arr = np.delete(arr, i) 
    return arr



a = np.array([5, 3, 8, 3, 1, 5, 8, 2, 9, 1, 5, 3])
print(remove_duplicates(a)) 
print(remove_duplicates2(a)) 
print(remove_duplicates3(a)) 

