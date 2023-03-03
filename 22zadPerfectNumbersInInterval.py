n = 1
m = 30
perfect_num = 0
if n < 1:
    print(False)
else:
    for number in range (n,m+1):
        for i in range(n,m+1):
            if number%i == 0 and number != i:
                perfect_num +=i
        if perfect_num == number:
            print(number)
            perfect_num = 0
        else:
            perfect_num = 0

