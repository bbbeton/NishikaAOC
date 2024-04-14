floor = 0
counter = 0
with open('input.txt') as file:
    for line in file:
        line = line.strip() # remove newline character
        for char in line:
            if floor != -1:
                if char == '(':
                    floor += 1
                elif char == ')':
                    floor -= 1
                counter += 1
print(floor)
print(counter)