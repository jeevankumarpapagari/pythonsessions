s = input()
l = [False,False,False,False,False]
for c in s:
    if c.isalnum():
        l[0] = True
    if c.isalpha():
        l[1] = True
    if c.isdigit():
        l[2] = True
    if c.islower():
        l[3] = True
    if c.isupper():
        l[4] = True
for x in l:
    print(x)
