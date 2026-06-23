# tail recursion - a recursion that starts execution from the end
count = 0

def call():
    global count
    if count==10:
        print(f"THIS IS COUNT {count}")
        return
    
    count+=1
    call()
    count-=1
    print(f"THIS IS COUNT {count}")

call()