f = open('letters.txt', 'r')

def hasLetterTwice(inputLine):
    for char in inputLine:
        if (inputLine.count(char) == 2):
            return True
    return False

def hasLetterTrice(inputLine):
    for char in inputLine:
        if (inputLine.count(char) == 3):
            return True
    return False

twoCounter = 0
threeCounter = 0

for line in f:
    if hasLetterTwice(line):
        twoCounter = twoCounter + 1
    if hasLetterTrice(line):
        threeCounter = threeCounter + 1

print twoCounter * threeCounter
f.close()

