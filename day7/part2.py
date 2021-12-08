''' Link to challenge prompt: https://adventofcode.com/2021/day/7
Same code as last one, except the fuel calculation is a bit more complicated.
Took me much longer than I would like to admit to figure out the problem was a
perfect case for recursion...
'''
import sys

def calculate_total_fuel(alignment, crabs):
    total_fuel = 0
    for crab in crabs:
        total_fuel +=  calculate_fuel(abs(alignment - crab))
    return total_fuel

def calculate_fuel(distance):
    if distance == 0: return 0
    # Base case
    if distance == 1: return 1
    # The fuel cost to travel a distance is the distance travelled + the fuel
    # cost to travel 1 less distance
    return calculate_fuel(distance - 1) + distance

crabs = list(map(int, open('input.txt').readline().split(','))) 
# Kept reaching max recursion depth, but I really like the recursion... Python
# will allow me to set the max recursion depth past 1000. Ends up being a bit
# slower than it probably should be, but the code is way prettier than iteration
# so we keep it 
sys.setrecursionlimit(max(crabs) + 3)
costs = {}
for alignment in range(crabs[len(crabs)-1]):
    costs[alignment] = calculate_total_fuel(alignment, crabs)
# The key argument in min is the comparison operator to use to calculate the min. 
print(costs[min(costs, key=costs.get)])