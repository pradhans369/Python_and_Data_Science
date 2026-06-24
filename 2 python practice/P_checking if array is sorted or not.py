import numpy as np
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

def check(lst):
    for i in range(len(lst)-1):
        if lst[i] > lst[i + 1]:
            return False
    
    return True

print(check(a))



