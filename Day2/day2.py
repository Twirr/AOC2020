def part1():
    f=open("Day2/input.txt", "r")

    lines = f.readlines()

    count = 0
    for line in lines:
        count += handleline(line)

    print(count)   

def handleline(line):
    args = line.split()
    minmax = args[0].split('-')
    charToCount = args[1].replace(":","")
    return validate(int(minmax[0]),int(minmax[1]),charToCount,args[2])


def validate(min,max,char,password):
    occurences = password.count(char)
    if occurences >= min and occurences <= max:
        return 1
    else:
        return 0 

import time
start_time = time.time()
part1()
print("--- %s seconds ---" % (time.time() - start_time))   