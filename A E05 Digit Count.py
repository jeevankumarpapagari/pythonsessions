n = int(input())
if n==0:
    print(1)
else:
    dc = 0
    while n!=0:
        dc += 1
        n //= 10
    print(dc)
