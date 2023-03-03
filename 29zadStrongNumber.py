import math
reminder = 0
n = 145
sum = 0
tmp = n

while n != 0:
    #shrink the number
    reminder = n % 10
    #factorial
    fact = 1
    for i in range(2,n+1):
        fact *= i
    #add factorial to sum
    sum += fact
    n = math.floor(n/10)
if sum == tmp:
    print(tmp," is a strong num")
else:
    print(tmp," is not a strong num")
    