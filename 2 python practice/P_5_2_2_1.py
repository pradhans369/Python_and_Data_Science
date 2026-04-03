
x = 121

if x < 0:
    print(False)


temp = x 
reversed = 0

while temp > 0:
    digit = temp % 10
    reversed = (reversed * 10) + digit
    temp  = temp // 10


print(f"REVERSED DIGIT : {reversed}")


if x == reversed:
    print(True)
else:
    print(False)








