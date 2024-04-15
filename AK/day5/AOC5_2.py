sum = 0


file = open('inputAOC5.txt', 'r')
while 1:
    containsCheck = 0
    doubleCheck = 0
    line = file.readline()
    if not line: 
        break
    
    for i in range(0,len(line)):

        twoChars = line[i-1] + line[i]
        if line.count(twoChars) >= 2:
            containsCheck = 1
        if line[i] == line[i-2]:
            doubleCheck = 1
        if containsCheck and doubleCheck:
            sum += 1
            break

print(sum)