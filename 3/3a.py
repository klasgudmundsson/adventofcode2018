import re

f = open('fabrics.txt', 'r')

fabricArray = [[0 for x in range(1000)] for y in range(1000)]

for line in f:
    regexString = r'^#\d{1,4} @ (\d{1,3}),(\d{1,3}): (\d{1,3})x(\d{1,3})'
    m = re.search(regexString, line)
    xCoord = int(m.group(1))
    yCoord = int(m.group(2))
    xWidth = int(m.group(3))
    yWidth = int(m.group(4))

    for x in range (0, xWidth):
        for y in range (0, yWidth):
            fabricArray[x + xCoord][y + yCoord] += 1

patchesWithCountLargerThanOne = 0
for x in range (0, 1000):
        for y in range (0, 1000):
            if fabricArray[x][y] > 1:
                patchesWithCountLargerThanOne += 1

print patchesWithCountLargerThanOne
f.close()