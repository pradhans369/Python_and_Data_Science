n = 123456

def extract(num):
    temp_list = []
    while num > 0:
        last_digit = num % 10
        new_num = num // 10
        num = new_num
        temp_list.append(last_digit)
    
    return sorted(temp_list)

print(extract(n))





