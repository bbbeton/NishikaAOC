import re

file = open('input.txt')

l = 0
w = 0
h = 0
sum = 0
sumRibbon = 0

content = file.readlines()

for line in content:
    out = re.split('x',line)
    res = [eval(i) for i in out]
    l = res[0]
    w = res[1]
    h = res[2]
    res.sort()
    sum += 2*l*w + 2*w*h + 2*h*l + min(l*w,w*h,h*l)
    sumRibbon += l*w*h + 2*res[0] + 2*res[1]

print(f"2_1 {sum}")
print(f"2_2 {sumRibbon}")