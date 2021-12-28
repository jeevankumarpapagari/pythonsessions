import array as arr
a = arr.array('i',list(map(int,input().split())))
for ele in a:
    print(ele,end=" ")
    
#OR

l = list(map(int,input().split()))
for ele in l:
    print(ele,end=" ")

    
#OR

l = [int(x) for x in input().split()]
for ele in l:
    print(ele,end=" ")
