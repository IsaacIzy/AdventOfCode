# Link to challenge: https://adventofcode.com/2021/day/3#part2
# Challenge is a bit more complicated, so actually make an effort to compartmentalize code

def get_oxygen_rating(data):
    index = 0
    # Keep filtering out values until only 1 is left, which is the oxygen generator rating
    while len(data) > 1:
        most_common = get_most_interesting_bit(data, index, 'oxygen')
        data = filter_data(data, index, most_common)
        index += 1
    
    return bits_to_int(data[0])

def get_CO2_rating(data):
    index = 0
    # Keep filtering out values until only 1 is left, which is the CO2 scrubber rating
    while len(data) > 1:
        most_common = get_most_interesting_bit(data, index, 'CO2')
        data = filter_data(data, index, most_common)
        index += 1
    
    return bits_to_int(data[0])

'''
Converts a bit string into an integer
bits: bit string to convert
'''
def bits_to_int(bits):
    result = 0
    for bit in bits:
        result = (result << 1) | int(bit)
    return result

'''
Calculates the most "interesting" bit, according to the context provided
data: list of bit strings
index: index to check for most "interesting" bit
context: which function called this, oxygen or CO2. If Oxygen called, return most common bit, if CO2 called, return least common bit
'''
def get_most_interesting_bit(data, index, context):
    count = 0
    for entry in data:
        if entry[index] == '1':
            count += 1
    result = ''
    # Challenges specifies that if there are an equal number of 1s and 0s, use 1 if its oxygen rating, 0 if its CO2 rating
    if count == len(data)/2:
        result = '1' if context == 'oxygen' else '0'
    elif count < len(data)/2:
        # Oxygen context returns most common bit, Co2 context returns least common bit 
        result = '0' if context == 'oxygen' else '1'
    else:
        result = '1' if context == 'oxygen' else '0'
    return result

'''
Filters out values from a list of bit strings based on what value each string has at the specified index
data: list of bit strings
index: index to filter on
value: value to filter with
'''
def filter_data(data, index, value):
    filtered_data = []
    for entry in data:
        if entry[index] == value:
            filtered_data.append(entry)
    return filtered_data

if __name__ == '__main__':
    data = []
    with open('input.txt') as input:
        for entry in input:
            data.append(entry.strip())

    oxygen_rating = get_oxygen_rating(data)
    CO2_rating = get_CO2_rating(data)
    print(f'Oxy rating: {oxygen_rating}\nCO2 rating: {CO2_rating}')

    print(f'Solution: {CO2_rating * oxygen_rating}') 