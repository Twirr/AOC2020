def part2():
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
    
    if len(password) >= max:
        maxChar = password[max-1]
        maxMatches = maxChar == char
    else:
        maxMatches = False
        
    if len(password) >= min:
        minChar = password[min-1]
        minMatches = minChar == char
    else:
        minMatches = False

    return minMatches ^ maxMatches


import time
start_time = time.time()
part2()
print("--- %s seconds ---" % (time.time() - start_time))   