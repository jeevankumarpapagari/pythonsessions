result = 1
numberOfZeros = 0
for i in range(int(input())):
    n = int(input())
    while n%10==0:
        numberOfZeros += 1
        n //= 10
    result *= n
print(result,end="")
for i in range(numberOfZeros):
    print(0,end="")
        
