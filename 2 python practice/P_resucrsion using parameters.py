
# x = what number to print
# n = how many times to print the n

count = 0
def recursion(x,n):
    global count
    if count >= n:
        return

    count+=1
    print(x)
    recursion(x+1, n)



def recursion2(x,n, current_count=0):

    if current_count==n:
        print(x)
        return

    recursion2(x-2,n,current_count+1)
    print(x)




recursion(0, 5)
print('================================')
recursion2(10, 5)
