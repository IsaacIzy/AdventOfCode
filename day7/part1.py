''' Link to challenge prompt: https://adventofcode.com/2021/day/7
Super overthought this one... Also my initial implementation had a critical
error, but I got lucky with my input that the error was never reached lol.
Didn't found out until part2
'''
def calculate_total_fuel(alignment, crabs):
    fuel_cost = 0
    for crab in crabs:
        fuel_cost +=  abs(alignment - crab)
    return fuel_cost

crabs = list(map(int, open('input.txt').readline().split(','))) 
costs = {}
for alignment in range(crabs[len(crabs)-1]):
    costs[alignment] = calculate_total_fuel(alignment, crabs)
print(min(costs, key=costs.get))