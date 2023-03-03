import math
reversedNum = 0
n = 123456
lastDigit = 0

while n != 0:
    lastDigit = n%10
    reversedNum = reversedNum*10+lastDigit
    n = math.floor(n/10)

print(reversedNum)