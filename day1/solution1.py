data = []
with open('data.txt') as file:
    for line in file:
        data.append(int(line))

increased_count = 0
for i in range(len(data)-1):
    if data[i] < data[i+1]:
        increased_count += 1
print(increased_count)






