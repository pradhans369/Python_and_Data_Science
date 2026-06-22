n = 54536168465

# type 1
def check(num):
    temp_list = []
    while num != 0:
        digit = num % 10
        new_num = num // 10
        num = new_num

        temp_list.append(digit)
    
    return len(temp_list)


def check2(num):
    count = 0
    while num != 0:
        new_num = num // 10
        num = new_num
        count += 1
    return count


# --------------------------------------------------------------
# type 3 (good for time complexity)
from math import *
def check3(num):
    return int(log10(num) + 1)




print('check : ', check(n))
print('check2 : ', check2(n))
print('check3 : ', check3(n))


