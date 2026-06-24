P# counting vowels

a = input('enter the string : ')

vowels = 'aeiou'
count = 0

for i, char in enumerate(a):
    if char.lower() in vowels:
        print(f"Vowel '{char}' found at index {i}")
        count += 1
    
else:
    print('no vowels found')

