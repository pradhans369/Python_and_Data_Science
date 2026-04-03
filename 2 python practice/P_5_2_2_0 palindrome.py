a = [1,2,1]

copyOfa = a.copy()
copyOfa.reverse()

if a == copyOfa:
    print('this is a palindrome')
else:
    print('not a palindrome')

print('**********************************')

str = 'racecar'

if str == str[::-1]:    # [start : stop : step]

    '''
    s[::-1] means:

        start at the end of the string,
        move backwards (-1 step),
        go until the beginning.

        It creates a reversed copy of the string.

    '''

    print('this is a palindrome')
else:
    print('not a palindrome')
