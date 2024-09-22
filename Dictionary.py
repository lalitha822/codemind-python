s = "abaabcdcaba"
#    012345678910
# d = {'a': [0, 2, 3, 8, 10], 'b': [1, 4, 9], 'c': [5, 7], 'd': [6]}
d = {}
for i in range(len(s)):
    if s[i] in d:
        d[s[i]].append(i)
    else:
        d[s[i]] = [i]
print(d)
