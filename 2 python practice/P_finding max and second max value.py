import numpy as np

a = np.array([6,5,48,9,2,1,9,3,0,0,6,96,2,59,3,5,-1,999])

  
def find_max(arr):
    max = 0
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]

    return max


def find_max_and_max2(arr):
    if len(arr) < 2:
        raise ValueError("Array must contain at least 2 elements")
    
    max = 0
    max2 = 0

    for i in range(len(arr)):
        if arr[i] > max:
            max2 = max
            max = arr[i]
        elif arr[i] != max and arr[i] > max2:
            max2 = arr[i]

    return int(max), int(max2)


def max_max2(arr):
    max_val = 0
    max2_val = 0
    for i in range(len(arr)):
        max2_val = max(max2_val, min(max_val, arr[i]))        
        max_val = max(max_val, arr[i])

    return int(max_val), int(max2_val)



print(find_max(a))
print(find_max_and_max2(a))
print(np.max(a))
print(max_max2(a))