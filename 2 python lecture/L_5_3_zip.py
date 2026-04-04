"""
zip() is a built-in function in Python.
It takes two or more iterables (like lists, tuples, sets, or strings) and pairs their elements together index by index.
It returns an iterator of tuples.

It stored two or more lists at a time 

"""

names = ["Alice", "Bob", "Charlie"]
tricks = ["Card trick", "Levitation", "Disappearing act"]
names2 = ["Alice", "Bob", "Charlie"]

zipped = zip(names, tricks, names2)

print(zipped)               # will show memory location
print(list(zipped))
print('***************************************************************************')

# zip in for loop
for a, b in zip(names, tricks):
    print(f"{a} : {b}")
print('***************************************************************************')

# zip takes values in pairs
x = [1, 2, 3]
y = ['a', 'b']
print(list(zip(x, y)))      # It doesn’t throw error — it just stops.
print('***************************************************************************')

# unzipping -- reverse operation
pairs = [(1, 'a'), (2, 'b')]        # now the values are stored in zip format
nums, letters = zip(*pairs)         # stores first element of each pair in nums, and second pair of each pair in letters
print(nums)
print(letters)
print('***************************************************************************')

# working with three lists
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
print(list(zip(a, b, c)))  # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]

