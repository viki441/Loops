import math
number = 7
counter = 0

for i in range (1,number):
    if number/i == math.trunc(number/i):
        counter +=1
if counter > 2 or number == 1:
    print('not prime')
else:
    print('prime')