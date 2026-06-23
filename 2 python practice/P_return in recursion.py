

def sum(n, total=0,count=0):
    if count>n:
        return total

    total+=count
    count+=1
    return sum(n,total,count)


def sum2(n, total=0,count=0):
    if count>n:
        return total

    return sum2(n, total+count, count+1)

# best for time and space compelxity
def sum3(n):
    if n==0:
        return 0
    
    return n + sum3(n-1)

# best for time and space compelxity
def factorial(n):
    if n==0 or n==1:
        return 1
    
    return n * factorial(n-1)



print(sum(10))
print(sum2(15))
print(sum3(4))
print(factorial(5))