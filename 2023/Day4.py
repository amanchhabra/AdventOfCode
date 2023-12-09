import re


# Puzzle 1
def solve_puzzle1():
    count = 0
    while True:
        line = input()
        if line:
            results = re.search('Card\s+(\d+): ([\d\s]+) \| ([\d\s]+)', line)
            winning_numbers = [int(data) for data in re.findall('\d+', results.group(2))]
            numbers = [int(data) for data in re.findall('\d+', results.group(3))]
            win = [number for number in numbers if number in winning_numbers]
            if len(win) > 0:
                count = count + 2 ** (len(win) - 1)

        else:
            print(count)
            break


# Puzzle 2
def solve_puzzle2():
    count = 0
    inputs = []
    while True:
        for i in range(300):
            inputs.append(0)
        line = input()
        if line:
            results = re.search('Card\s+(\d+): ([\d\s]+) \| ([\d\s]+)', line)

            winning_numbers = [int(data) for data in re.findall('\d+', results.group(2))]
            numbers = [int(data) for data in re.findall('\d+', results.group(3))]
            win = [number for number in numbers if number in winning_numbers]
            card_number = int(results.group(1))
            if len(win) > 0:
                inputs[card_number] = inputs[card_number] + 1
                for y in range(inputs[card_number]):
                    for x in range(len(win)):
                        inputs[x + card_number + 1] = inputs[x + card_number + 1] + 1

            else:
                inputs[card_number] = inputs[card_number] + 1
        else:
            for card in inputs:
                count = count + card
            print(count)
            break


solve_puzzle2()
