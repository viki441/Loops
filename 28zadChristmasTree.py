n = 4
pattern = ''
index = 0

#first |
for first in range(0,n):
    #add n times blank space
    pattern += ' '
#in the middle add:
pattern += ' | '
#rest of symbols:
for i in range(1,n):
    #fisrt add a new line
    pattern += "\n"
    #we need a variable (index) to count how many
    #times we add blank space (for each line the number is 
    #going to be smaller, because of the more stars)
    index += 1

    for space in range(index,n+1):
        #add blank space
        pattern += " "
    for a in range(0,i):
        #this one adds stars BEFORE the line |
        #a is compared to i, because i doen't reset
        pattern += '*'

    #add a line in the middle
    pattern += "|"
    for b in range(0,i):
        #this one is for AFTER the line
        pattern += "*"

print(pattern)