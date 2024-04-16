filename = 'input.txt'
l = 0
w = 0
h = 0
sum = 0
with open(filename) as file:
    for line in file:
        line = line.strip()
        line = line.split('x')
        l = int(line[0])
        w = int(line[1])
        h = int(line[2])
        sum += 2 * l * w + 2 * w * h + 2 * h * l + min(l * w, w * h, h * l)
print(sum)