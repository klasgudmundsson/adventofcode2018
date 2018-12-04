import re

f = open('fabrics.txt', 'r')

fabricArray = [[0 for x in range(1000)] for y in range(1000)]

def firstLoop(file, arr):
    for line in file:
        regexString = r'^#(\d{1,4}) @ (\d{1,3}),(\d{1,3}): (\d{1,3})x(\d{1,3})'
        m = re.search(regexString, line)
        id = int(m.group(1))
        xCoord = int(m.group(2))
        yCoord = int(m.group(3))
        xWidth = int(m.group(4))
        yWidth = int(m.group(5))
        
        for x in range (0, xWidth):
            for y in range (0, yWidth):
                arr[x + xCoord][y + yCoord] += 1

    return arr

def secondLoop(file, arr):
    for line2 in file:
        regexString = r'^#(\d{1,4}) @ (\d{1,3}),(\d{1,3}): (\d{1,3})x(\d{1,3})'
        m = re.search(regexString, line2)
        id = int(m.group(1))
        xCoord = int(m.group(2))
        yCoord = int(m.group(3))
        xWidth = int(m.group(4))
        yWidth = int(m.group(5))
        
        notOverlapping = True
        for x in range (0, xWidth):
            for y in range (0, yWidth):
                if(arr[x + xCoord][y + yCoord] != 1):
                    notOverlapping = False
        if (notOverlapping):
            print id

fabricArray = firstLoop(f,fabricArray)
f.seek(0) #Reset the file's current position, at this point the pointer points to the end of the file.
secondLoop(f,fabricArray)
f.close()
