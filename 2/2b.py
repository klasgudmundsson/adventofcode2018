import re
from itertools import islice

f = open('letters.txt', 'r')

def checker(inputLine, file):
    lineLength = len(inputLine)
    for line in file:
        regexStr = '.+' + inputLine[1:]
        m = re.match(regexStr, line)
        if (m):
            return line, inputLine
        for charIndex in range (1,lineLength):
            regexStr = inputLine[0:charIndex] + '.+' + inputLine[charIndex+1:]
            m = re.match(regexStr, line)
            if (m):
                return line, inputLine
    return False

listWithFile = []
for line in f:
    listWithFile.append(line)

for index in range (0, len(listWithFile)):
    listToPass = []
    for line in listWithFile[0:index]:
        listToPass.append(line)
    for line in listWithFile[index+1:]:
        listToPass.append(line)
    if(checker(listWithFile[index], listToPass)):
        res1, res2 = checker(listWithFile[index], listToPass)
        print res1
        print res2
        break

f.close()
