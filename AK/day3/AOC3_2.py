array = []
x = 0
y = 0
xRobo = 0
yRobo = 0
sum = 1
switch = False

array.append([x,y,False])
array.append([xRobo,yRobo,False])

file = open('inputAOC3.txt', 'r')

while 1:
    step = file.read(1)          
    if not step: 
        break

    match step:
        case '^': 
            if switch == False:
                y += 1 
            else:
                yRobo += 1
        case '<':
            if switch == False:
                x -= 1 
            else:
                xRobo -= 1
        case 'v':            
            if switch == False:
                y -= 1 
            else:
                yRobo -= 1
        case '>':            
            if switch == False:
                x += 1 
            else:
                xRobo += 1
    
    
    if switch == False:
        if [x,y,False] in array:
            array.append([x,y,True])
        else:
            array.append([x,y,False])   
            sum += 1
    else:
        if [xRobo,yRobo,False] in array:
            array.append([xRobo,yRobo,True])
        else:
            array.append([xRobo,yRobo,False])
            sum += 1
    switch = not switch


print(sum) 
