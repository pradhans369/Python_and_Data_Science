n = 121

def palindrome(num):
    if num == 0:
        return False

    original_num = num
    reverse_num = 0
    while num > 0:
        last_digit = num % 10
        num //= 10

        reverse_num = (reverse_num * 10) + last_digit

    return original_num == reverse_num


print(palindrome(n))


