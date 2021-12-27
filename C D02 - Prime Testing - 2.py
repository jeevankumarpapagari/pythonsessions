from math import sqrt
for i in range(int(input())):
    n = int(input())
    count = 0
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            count = 1
            break
    print("yes") if count == 0 and n!=1 else print("no")
