l = [int(x) for x in input().split()]
for i in range(-1,-len(l)-1,-1):
    print(l[i],end=" ")
    
#OR

l = [int(x) for x in input().split()]
l = l[::-1]
for i in l:
    print(i,end=" ")

#OR

l = [int(x) for x in input().split()]
for i in range(len(l)-1,-1,-1):
    print(l[i],end=" ")
