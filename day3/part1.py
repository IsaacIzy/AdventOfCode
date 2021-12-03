# Link to challenge: https://adventofcode.com/2021/day/3
data = []
with open('input.txt') as input:
    for line in input:
        data.append(line.strip())

# Array to count all of the '1' values in each column of the input
position_counts = []
for i in range(len(data[0])-1):
    # Need to initialize each column to 0
    position_counts.append(0)
    for entry in data:
        if entry[i] == '1':
            position_counts[i] = position_counts[i] + 1

# Once all the counts are collected, calculate gamma and epsilon
gamma_bits = []
epsilon_bits = []
input_size = len(data)
for count in position_counts:
    # Count is the total number of 1s that showed up in that column of the input.
    # Challenge does not specify what to do if there is an equal number of 0s and 1s, so assume 1 if equal
    if count >= input_size/2:
        gamma_bits.append(1)
        epsilon_bits.append(0)
    else:
        gamma_bits.append(0)
        epsilon_bits.append(1)

# Convert gamma and epsilon from a list of bits to an integer. From: https://stackoverflow.com/questions/12461361/bits-list-to-integer-in-python
# Uses bitwise operators add all the bits to the int one by one. bitshifts gamma to the left, then adds the next bit on. Very slick
gamma = 0
for bit in gamma_bits:
    gamma = (gamma << 1) | bit
epsilon = 0
for bit in epsilon_bits:
    epsilon = (epsilon << 1) | bit

# calculate power consumption, which is just gamma * epsilon, and print the result
print(gamma * epsilon)