def surface_count(dimmensions):
    dimmensions = dimmensions.split("x")
    l = int(dimmensions[0])
    w = int(dimmensions[1])
    h = int(dimmensions[2])
    surface = 2*l*w + 2*l*h + 2*w*h
    if l*w <= l*h and l*w <= w*h:
        surface += l*w
    elif l*h <= l*w and l*h <= w*h:
        surface += l*h
    else:
        surface += w*h
    return surface

def ribbon_count(dimmensions):
    dimmensions = dimmensions.split("x")
    l = int(dimmensions[0])
    w = int(dimmensions[1])
    h = int(dimmensions[2])
    if l <= h and w <= h:
        ribbon = 2*l + 2*w
    elif w <= l and h <= l:
        ribbon = 2*w + 2*h
    else:
        ribbon = 2*l + 2*h
    ribbon += w*l*h
    return ribbon

with open("day_two_input.txt") as file:
    input = file.readlines()

total_surface = 0
total_ribbon = 0
for box in input:
    box_surface = surface_count(box)
    total_surface += box_surface

    ribbon_length = ribbon_count(box)
    total_ribbon += ribbon_length

print(total_surface, total_ribbon)
