
with open('input.txt') as input:
    costs = {1:0, 4:0, 7:0, 8:0}
    for line in input:
        _, output = line.split('|')
        output = output.split()
        for digit in output:
            if(len(digit)) == 2: 
                print(f'Digit {digit} found')
                costs[1] += 1
            if(len(digit)) == 4: 
                print(f'Digit {digit} found')
                costs[4] += 1
            if(len(digit)) == 3:
                print(f'Digit {digit} found')
                costs[7] += 1
            if(len(digit)) == 7:
                print(f'Digit {digit} found')
                costs[8] += 1
    print(sum(costs.values()))
        