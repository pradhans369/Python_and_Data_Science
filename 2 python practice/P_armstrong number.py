# different armstrong numbers are : 153,370,371,407,1634

n = 370

def armstrong(num):
    og = num
    temp_list = []

    while num > 0:
        last_digit=num % 10
        num//=10
        temp_list.append(last_digit)

    power=len(temp_list)
    temp_num=0
    for num in temp_list:
        temp=num ** power
        temp_num+=temp
    
    return temp_num == og


# best for time and space complexity
def armstrong2(num):
    og = num
    power = len(str(num))

    total=0
    while num > 0:
        last_digit=num % 10
        num//=10
        total+=(last_digit**power)

    return og==total



print(armstrong(n))
print(armstrong2(n))
