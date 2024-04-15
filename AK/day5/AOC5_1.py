vowels = "aeiou"
naughty = ['ab', 'cd', 'pq', 'xy']
sum = 0


file = open('inputAOC5.txt', 'r')
while 1:
    vowelsCheck = 0
    doubleCheck = 0
    naughtyCheck = 0
    line = file.readline()
    if not line: 
        break
    
    for n in naughty:
        if n in line:
            naughtyCheck = 1
    if not naughtyCheck:
        for i in range(0,len(line)):
            for vowel in vowels:
                if line[i] == vowel:
                    vowelsCheck += 1
                    break
            if line[i] == line[i-1]:
                doubleCheck = 1
            if vowelsCheck >= 3 and doubleCheck:
                sum += 1
                print(line)
                break

print(sum)