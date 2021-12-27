n = int(input())
count = 0
for i in range(1,n+1):
    if n%i==0:
        count += 1
print("Yes") if count == 2 else print("No")

#OR

n = int(input())
print("Yes") if all(n%i!=0 for i in range(2,n+1)) else print("No")
