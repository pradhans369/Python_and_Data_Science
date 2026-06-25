
haystack = "sadbutsad"
needle = "sad"

n = len(haystack)
m = len(needle)

for i in range(n - m + 1):
    temp = haystack[i : i + m]
    if temp == needle:
        print(i)
