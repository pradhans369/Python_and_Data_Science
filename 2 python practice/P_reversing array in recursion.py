
import numpy as np

a = np.array([1,2,3,4,5,6,7])

def reverse(arr, left, right):
    if left >= right:
        return a

    arr[left], arr[right] = arr[right], arr[left]

    return reverse(arr, left+1, right-1)

print(reverse(a, 0, len(a)-1))

print(reverse(a,2,4))
print(a[-1])
