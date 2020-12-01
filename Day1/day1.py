def solution():
    f=open("Day1/input.txt", "r")

    lines = f.readlines()

    values = set()
    result = []

    for l in lines:
        value = int(l)
        potentialMatch = 2020-value
        if potentialMatch in values:
            result.append((value,potentialMatch))
        else:
            values.add(value)
                
    for r in result:
        mult = r[0] * r[1]
        print(mult)

def solution2():
    f=open("Day1/input.txt", "r")

    lines = f.readlines()

    values = []
    doubleValues = {}
    result = []

    for l in lines:
        value = int(l)
        values.append(value)
        doubleValue = 2020-value

        doubleValues[doubleValue] = value

    for i in range(0,len(values)):
        for j in range(i,len(values)):
            sum = values[i] + values[j]
            if sum in doubleValues:
                result.append((doubleValues.get(sum),values[i],values[j]))

    for r in result:
        mult = r[0] * r[1] * r[2]
        print(mult)
    
def naiveSolution2():
    f=open("Day1/input.txt", "r")

    lines = f.readlines()

    values = []

    for l in lines:
        values.append(int(l))

    result = []
    for x in range(0, len(values)):
        for y in range(x,len(values)):
            for z in range(y,len(values)):
                sum = values[x]+values[y]+values[z]
                if sum == 2020:
                    result.append((values[x],values[y],values[z]))
                
    for r in result:
        mult = r[0] * r[1] * r[2]
        print(r[0],r[1],r[2])
        print(mult)

import time
start_time = time.time()
solution2()
print("--- %s seconds ---" % (time.time() - start_time))