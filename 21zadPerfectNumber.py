n = 10
sum = 0
for i in range(1,n):
    if n % i == 0:
        sum +=1
if sum == n:
    print(True)
else:
    print(False)
