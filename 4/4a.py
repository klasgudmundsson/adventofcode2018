import re
f = open('guards.txt', 'r')

# Find out what guard that sleeps the most
dateArray = []

for line in f:
    dateArray.append(line)
f.seek(0)

dateArray.sort() # Apparently, this will do the trick

#First, find out what guard (id) that sleeps the most
guardsSleepArray = [[0 for x in range(60)] for y in range(10000)] #One slot for each guard, up to 10000 guards. number indicates minutes slept
for element in dateArray:
    regexString = r'\[\d{4}-\d{2}-\d{2} (\d{2}):(\d{2})\] (\w{5}) #?(\d{1,4})?'
    m = re.search(regexString, element)
    hh = int(m.group(1))
    mm = int(m.group(2))
    keyWord = m.group(3)
    if (m.group(4)):
        id = int(m.group(4))
    if (keyWord == 'Guard'):
        continue
    elif (keyWord == 'falls'):
        minuteCounter = mm
    elif (keyWord == 'wakes'):
        for currentMinute in range (minuteCounter,mm):
            guardsSleepArray[id][currentMinute] += 1 # minutes slept by guard id at minutes minutecounter thorugh mm

currentGuardId = 0
currentGuardSum = 0
for guardId in range (10000):
    minutesSum = 0
    for minute in range (60):
        minutesSum += guardsSleepArray[guardId][minute]
    if minutesSum > currentGuardSum:
        currentGuardId = guardId
        currentGuardSum = minutesSum

minuteSleptMost = guardsSleepArray[currentGuardId][0:60].index(max(guardsSleepArray[currentGuardId][0:60]))
print 'Guard that slept the most: ' + str(currentGuardId)
print 'Minutes slept: ' + str(currentGuardSum)
print 'Minute that the guard slept the most: ' + str(minuteSleptMost)
print 'Total minutes slept that minute: ' + str(max(guardsSleepArray[currentGuardId][0:60]))
print guardsSleepArray[currentGuardId][0:60]
print 'Answer: ' + str(currentGuardId * minuteSleptMost)

f.close()