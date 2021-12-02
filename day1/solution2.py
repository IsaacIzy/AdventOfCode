data = []
with open('data.txt') as file:
    for line in file:
        data.append(int(line))

increased_count = 0
previous_sum = 0
for i in range(len(data)-1):
    if i  == len(data)-2: break
    sum = data[i] + data[i+1] + data[i+2]
    if previous_sum != 0 and previous_sum < sum:
        increased_count += 1
    previous_sum = sum
print(increased_count)

