import numpy as np
data = []
with open('input.txt') as input:
    for line in input:
        row = list(map(int, list(line.strip())))
        data.append(row) 
data = np.asarray(data, dtype=int)
sum = 0
for row in range(np.shape(data)[0]):
    for col in range(np.shape(data)[1]):
        # Check above
        if row > 0:
            if data[row][col] >= data[row-1][col]: continue
        # Check below
        if row < np.shape(data)[0]-1:
            if data[row][col] >= data[row+1][col]: continue
        # Check left
        if col > 0:
            if data[row][col] >= data[row][col-1]: continue
        # Check right
        if col < np.shape(data)[1]-1:
            if data[row][col] >= data[row][col+1]: continue
        sum += data[row][col] + 1
print(sum)