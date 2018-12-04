f = open('numbers.txt', 'r')
sum = 0
for line in f:
    sum = sum + int(line)
print sum
f.close()