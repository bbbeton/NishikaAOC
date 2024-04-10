array = []
x = 0
y = 0
sum = 1

file = open('inputAOC3.txt', 'r')

array.append([x,y,False])

while 1:
    step = file.read(1)          
    if not step: 
        break

    match step:
        case '^': y += 1
        case '<': x -= 1
        case 'v': y -= 1
        case '>': x += 1
    if [x,y,False] in array:
        array.append([x,y,True])
    else:
        array.append([x,y,False])
        sum += 1
   

        
print(sum) 