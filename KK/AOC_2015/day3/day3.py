def move(direction, x, y):
    if direction == '>':
        x -= 1
    elif direction == '<':
        x += 1
    elif direction == '^':
        y += 1
    elif direction == 'v':
        y -= 1
    return x, y


def count_visited(visited):
    repeated_pairs = []
    for pair in visited:
        if pair not in repeated_pairs:
            repeated_pairs.append(pair)
    return len(repeated_pairs)


def main():
    x = 0
    y = 0
    how_many = 0
    visited = [(x, y)]
    filename = 'input.txt'
    with open(filename) as file:
        for directions in file:
            directions = directions.split()
            for direction in directions:
                for character in direction:
                    x, y = move(character, x, y)
                    visited.append((x, y))

    how_many = count_visited(visited)
    print(how_many)

if __name__ == '__main__':
    main()
