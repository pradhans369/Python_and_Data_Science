
def sort(lst):
    n = len(lst)

    for i in range(n):
        for j in range(0, n-i-1):
                if lst[j] > lst[j + 1]:
                    lst[j], lst[j+1] = lst[j+1], lst[j]

    return lst




a = [5, 4, 3, 2, 1]
print(sort(a))