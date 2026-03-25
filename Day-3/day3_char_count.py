s = input("Enter string: ")
d = {}
for ch in s:
    if ch in d:
        d[ch] += 1
    else:
        d[ch] = 1
for key in d:
    print(key, ":", d[key])