for i in range(int(input())):
    n = int(input())
    for i in range(1,n+1):
        if n%i==0:
            print(i,end=" ")
    print()
