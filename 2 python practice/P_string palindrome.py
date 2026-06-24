
def palindrome(a,left=0,right=None):
    if right==None:
        right = len(a)-1

    if left >= right:
        return True

    if a[left] == a[right]:
        return palindrome(a, left+1, right-1)
    else:
        return False




word = 'maam'
print(word[1])
print(palindrome(word))


