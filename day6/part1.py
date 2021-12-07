'''
Link to challenge prompt: https://adventofcode.com/2021/day/6
Spent way too long on this one trying to optimize looping and appending to enormous lists, obviously causing some
performance issues for part 2... Ended up resorting to finding a hint on reddit, and now it seems so obvious. 
Since the fish have no unique data, they are just a number, there is no reason to have an entry in a list for every fish.
We can just use a dictionary with keys for every "gestation" value, and the number of fish at that gestation value. 
This way, we are only storing and operating on a dictionary with 10 keys instead of a list with billions of entries.
To simulate another day, simply move all the values 1 key lower, and overflow -1 to 8 and 6.

Solution could be MUCH cleaner, but this is relatively readable so we keep it :)
'''
import numpy as np

initial_fish = list(map(int, open('input.txt').readline().split(','))) 
fishies = {8:0, 7:0, 6:0, 5:0, 4:0, 3:0, 2:0, 1:0, 0:0, -1:0}
for fish in initial_fish:
    fishies.update({fish: fishies.get(fish) + 1})
# Start the simulation
for day in range(256):
    new_fishies = fishies.copy()
    for last_reproduced, value in fishies.items():
        if last_reproduced == -1:
            new_fishies.update({8: new_fishies.get(-1), 6: new_fishies.get(6) + new_fishies.get(-1), -1: 0})
        else:
            new_fishies.update({last_reproduced - 1: value})
    fishies = new_fishies.copy()
    print(f'After {day+1} day: {sum(fishies.values())}')

print(sum(fishies.values()))
