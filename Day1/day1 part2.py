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
    print(mult)
