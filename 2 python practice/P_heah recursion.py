count=0

# head recursion
def greet():
    global count            # calling the global variable
    if count == 10:
        return
    
    print(f"THIS IS COUNT {count}")
    count+=1
    greet()

# greet()

print('------------------------------------------')







