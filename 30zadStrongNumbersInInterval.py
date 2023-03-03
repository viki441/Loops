import math
reminder = 0
sum = 0
m = 200
tmp = 0

for n in range(1,m+1):
    tmp = n
    while n != 0:
        #shrink number
        reminder = n % 10
        #factorial
        fact = 1
        for i in range(2,reminder+1):
            fact *= i
        #add factorial to sum
        sum += fact
        n = math.trunc(n/10)
        
    #check sum
    if sum == tmp:
        print(tmp,' is a strong num')
        sum = 0
    else:
        sum = 0