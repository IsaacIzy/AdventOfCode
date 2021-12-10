'''
Link to challenge prompt: https://adventofcode.com/2021/day/8#part2
I am not proud of this code... Perhaps some of the ugliest I have ever produced,
but hey it works and I am getting behind on the challenges and I want to do one
every night so we move. Good refresher on a bit of set theory, my brain got very
confused on the difference between difference and symmetric difference and
created a bug that only happened on some inputs
'''

def decode(input):
    segments = {'top':None, 'top_left':None, 'top_right':None, 'mid':None, 'bot_left':None, 'bot_right':None, 'bot':None}
    decoded_digits = {0:None, 1:None, 2:None, 3:None, 4:None, 5:None, 6:None, 7:None, 8:None, 9:None}
    # 1,4,7,8 are all a unique number of segments, so we can set those right away
    decoded_digits[1] = input[0]
    decoded_digits[4] = input[2]
    decoded_digits[7] = input[1]
    decoded_digits[8] = input[9]
    # Next, we can figure out the top segment, the difference between 1 and 7
    segments['top'] = min(decoded_digits[1] ^ decoded_digits[7])
    # We can use that and the segments in 4 to figure out what zero is. Check
    # the 3 digits that have 6 segments to find out which is 0
    for wires in input[6:9]:
        # If 1s segments are a subset of wires segments AND the symmetric
        # difference of wires and 4 has 1 element, that element is mid and the
        # digit is 0
        if decoded_digits[1] <= wires and len(decoded_digits[4] - wires) == 1:
            decoded_digits[0] = wires
            segments['mid'] = min(decoded_digits[4] - wires)
    # 1s segments are a subset of 9, and are not a subset of 6
    for wires in input[6:9]:
        if wires == decoded_digits[0]: continue
        elif decoded_digits[1] <= wires:
            decoded_digits[9] = wires
        else:
            decoded_digits[6] = wires
            segments['bot_right'] = min(decoded_digits[1] & decoded_digits[6])
            segments['top_right'] = min(decoded_digits[1] - decoded_digits[6])
    # we can figure out top_left segment from 4 since there is only 1 segment
    # left to figure out for 4
    known_segments = {segments['top_right'],segments['mid'],segments['bot_right']}
    segments['top_left'] =  min(known_segments ^ decoded_digits[4])
    # we can figure out bottom segment from 9
    known_segments = {segments['top'],segments['top_left'],segments['top_right'],segments['mid'],segments['bot_right']}
    segments['bot'] =  min(known_segments ^ decoded_digits[9])
    # That leaves 1 segment left unknown, bot_left.
    known_segments = {segments['top'],segments['top_left'],segments['top_right'],segments['mid'],segments['bot_right'],segments['bot']}
    segments['bot_left'] = min(decoded_digits[8] ^ known_segments)
    # Now we know 2, 3, and 5
    decoded_digits[2] = {segments['top'],segments['top_right'],segments['mid'],segments['bot_left'],segments['bot']}
    decoded_digits[3] = {segments['top'],segments['top_right'],segments['mid'],segments['bot_right'],segments['bot']}
    decoded_digits[5] = {segments['top'],segments['top_left'],segments['mid'],segments['bot_right'],segments['bot']}
    return decoded_digits

def sort_wires(wires_list):
    for i in range(len(wires_list)):
        wires_list[i] = set(sorted(wires_list[i]))
    return wires_list
    
with open('input.txt') as data:
    outputs = []
    for line in data:
        input, output = line.split('|') 
        input = sort_wires(input.split())
        output = sort_wires(output.split())
        input = list(sorted(input, key=len))
        decoded_digits = decode(input)
        value = ''
        for out_digit in output:
            for in_digit in decoded_digits.keys():
                if out_digit == decoded_digits[in_digit]:
                    value = value + str(in_digit)
                    break
        print(value)
        outputs.append(int(value))
    print(sum(outputs))
