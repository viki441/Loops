n = 5
pyramid = ''

for i in range(0,n):
    for j in range(0,i):
        pyramid += "$"
    pyramid += "\n"

print(pyramid)