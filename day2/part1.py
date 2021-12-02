with open('input.txt') as input:
    depth = 0
    position = 0
    for move in input:
        direction, distance = move.split(' ')
        distance = int(distance)
        if direction == 'forward':
            position += distance
        elif direction == 'up':
            depth -= distance
        elif direction == 'down':
            depth += distance
    print(depth * position)
            