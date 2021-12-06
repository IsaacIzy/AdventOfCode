'''
Link to challenge prompt: https://adventofcode.com/2021/day/5#part2
This part will be exactly the same code, except get_coords will be improved to handle diagonal lines
Code is quite ugly because I forgot how to do algebra for a bit there LMAO. But the solution works and it isn't terribly inefficient
'''
import numpy as np

'''
Takes a vector and returns a list of tuples, each tuple representing an x,y coordinate pair
start: Tuple with the vector starting coordinate
end: Tuple with the vector ending coordinate
returns: list of tuples representing the coordinates along the line segment
'''
def get_coords(start, end):
    x1, y1 = start
    x2, y2 = end
    # Case if horizontal line. Easy calculation
    if y1 == y2: 
        coords_list = [(x, y1) for x in (range(x1, x2+1) if x1 < x2 else range(x2, x1+1))]
        return coords_list
    # Case if vertical line, also easy
    if x1 == x2:
        coords_list = [(x1, y) for y in (range(y1, y2+1) if y1 < y2 else range(y2, y1+1))]
        return coords_list
    # good ol y = mx + b time. Calculate m, which will either be 1 or -1, then use that to calculate b
    m = int((y1-y2)/(x1-x2))
    b = int(y1 - m*x1)
    # now calculate all possible coordinates using y = mx + b, but only keep the ones that fit into the bounding box created by the start and end coords
    coords_list = []
    # Solve for y using all the possible x values
    for x in (range(x1, x2+1) if x1 < x2 else range(x2, x1+1)):
        y = int(m*x + b)
        # check if the coordinate is within our start and end coords
        if (x >= (x1 if x1 <= x2 else x2) and 
            x <= (x2 if x2 >= x1 else x1) and 
            y >= (y1 if y1 <= y2 else y2) and 
            y <= (y2 if y2 >= y1 else y1)):
            coords_list.append((x,y))
    # Solve for x using all the possible y values
    for y in (range(y1, y2+1) if y1 < y2 else range(y2, y1+1)):
        x = int((y - b)/m)
        if (x >= (x1 if x1 <= x2 else x2) and 
            x <= (x2 if x2 >= x1 else x1) and 
            y >= (y1 if y1 <= y2 else y2) and 
            y <= (y2 if y2 >= y1 else y1) and
            (x, y) not in coords_list):
            coords_list.append((x,y))
    return coords_list
    


coords_list = []
with open('input.txt') as input:
    # keep track of the largest value for x and y so we know how big of an ndarray we need
    largest_x = 0
    largest_y = 0
    for line in input:
        # Split the input line on the arrow to get the 2 coords as strings
        start_coordstr, end_coordstr = line.split('->')
        # Convert the strings to tuples of ints and check if we need to update largest x/y
        start_coord = tuple(map(int, start_coordstr.split(',')))
        end_coord = tuple(map(int, end_coordstr.split(',')))
        if start_coord[0] > largest_x: largest_x = start_coord[0]
        if start_coord[1] > largest_y: largest_y = start_coord[1]
        if end_coord[0] > largest_x: largest_x = end_coord[0]
        if end_coord[1] > largest_y: largest_y = end_coord[1]
        coords = get_coords(start_coord, end_coord)
        if coords != None:
            coords_list.extend(coords)
# Input has been parsed, now put all the points in a numpy ndarray
# Init ndarray with all zeros
points = np.zeros((largest_y+1, largest_x+1), dtype=int)
# Iterate over the list of coords and increment the value at that coord in the ndarray
for coord in coords_list:
    x, y = coord
    points[y][x] += 1
# Finally, count all the values > 1. Any comparison on an ndarray will return an array of booleans with the same shape. 
# pass that to count_nonzero() which will count all the "true" values, giving us our challenge answer
result = np.count_nonzero(points > 1)
print(result)