n = 21550

def factors(num):
    
    factors_list=[]
    for i in range(1,num+1):
        if num%i==0:
            factors_list.append(i)

    return factors_list


# best for time and space complexity
def factors2(num):
    temp_list=[i for i in range(1, (num//2) + 1) if num%i == 0]      # here we devided by 2 coz, the factors which can be found is atmost to the half of current num, except the number itself
    temp_list.append(num)
    return temp_list
    

# best for time and space complexity
from math import sqrt
def factors3(num):
    temp_list=[]
    for i in range(1, int(sqrt(num)) + 1):
        if num % i == 0:
            temp_list.append(i)
            if i != num // i:
                temp_list.append(num // i)

    return sorted(temp_list)


print(factors(n))
print(factors2(n))
print(factors3(n))
