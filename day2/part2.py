with open('input.txt') as input:
    depth = 0
    position = 0
    aim = 0
    for move in input:
        direction, distance = move.split(' ')
        distance = int(distance)
        if direction == 'forward':
            position += distance
            depth += aim * distance
        elif direction == 'up':
            aim -= distance
        elif direction == 'down':
            aim += distance
    print(depth * position)
 