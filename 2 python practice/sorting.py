
# ascending order
def sort(lst):
    n = len(lst)

    for i in range(0, n):
        for j in range(i+1, n):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]

    return lst


# descending order
def sort2(lst):
    n = len(lst)

    for i in range(0,n):
        for j in range(i+1,n):
            if lst[i] < lst[j]:
                lst[i], lst[j] = lst[j], lst[i]

    return lst

a = [1, 3, 2, 5, 4, 7, 6, 9, 8]
print(sort(a))
print(sort2(a))