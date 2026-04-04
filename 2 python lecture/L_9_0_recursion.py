# learning recursion

def show(n):
    if n==0:
        return
    
    print(n, end=' ')

    show(n-1)   # calling the function again, hence a recursion

show(5)






