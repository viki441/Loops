import math
number = 2
numberTo = 20
counter = 0

for number in range(number,numberTo):
    for i in range(1,number+1):
        if number/i == math.trunc(number/i):
            counter +=1
    if counter > 2 or number == 1:
        #doesn't print
        counter = 0
    else:
        counter = 0
        print(number)