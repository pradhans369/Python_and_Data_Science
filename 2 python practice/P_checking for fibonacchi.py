a = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# sending entire list
def check(list, first=0,second=1, result=2, last_index=None):
    if last_index==None:
        last_index = len(list)-1
    
    if result > last_index:
        return True
    
    
    if list[result] == (list[first] + list[second]):
        return check(list, first+1,second+1,result+1,last_index)
    else:
        return False

# sending a number
def check2(num,a=0,b=1):
    if num < 0:
        return False
    if num == a:
        return True
    if a > num:
        return False
    
    return check2(num, b, a+b)

print(check(a))
print(check2(4))
print(check2(5))
