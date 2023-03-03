n = 5
square = ''

for i in range(0,n):
    for j in range(0,n):
        #first and last line are full *
        if i == 0 or i == n-1:
            square += "*"
        #others have holes
        else:
            #add a * at the beginning and end
            if j == 0 or j == n - 1:
                square += "*"
            #if in the middle:
            else:
                square += " "
    square += "\n"
print(square)
    