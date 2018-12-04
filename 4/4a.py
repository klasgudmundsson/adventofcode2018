import re
f = open('guards.txt', 'r')

# Find out what guard that sleeps the most
dateArray = []

for line in f:
    dateArray.append(line)
f.seek(0)

dateArray.sort() # Apparently, this will do the trick

#First, find out what guard (id) that sleeps the most
guardsSleepArray = [0 for x in range(10000)] #One slot for each guard, up to 10000 guards. number indicates minutes slept
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
        guardsSleepArray[id] += mm - minuteCounter # minutes slept by guard id

print 'Guard that slept the most: ' + str(guardsSleepArray.index(max(guardsSleepArray)))
print 'Hours slept: ' + str(max(guardsSleepArray))

f.close()