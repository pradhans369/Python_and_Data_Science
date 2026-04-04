# merge two sorted list and make a sorted list

list1 = [1,2,4,4,6,7,54,7,8,4]
list2 = [1,3,4,8,4,3,1,]

temp = []
for i, j in zip(list1, list2):
    if i == j:
        temp.append(i)
    elif i < j:
        temp.append(i)
        temp.append(j)
    elif i > j:
        temp.append(j)
        temp.append(i)

temp.sort()


print(temp)

# limitation : the loop will stop once the shortest list ends, and ignore reset of the nums in the bigger list


