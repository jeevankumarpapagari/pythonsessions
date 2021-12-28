from math import factorial
n = factorial(int(input()))
digitCount = 0
while n!=0:
    digitCount += 1
    n //= 10
    
print(digitCount)

#OR

from math import factorial
print(len(str(factorial(int(input())))))
