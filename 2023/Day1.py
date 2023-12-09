import re


# Puzzle 1
def solve_puzzle1():
    count = 0
    while True:
        line = input()
        if line:
            results = re.findall('\d', line)
            number1 = get_number(results[0])
            number2 = get_number(results[-1])
            count = count + (number1 * 10 + number2)
        else:
            print(count)
            break


# Puzzle 2
def solve_puzzle2():
    count = 0
    while True:
        line = input()
        if line:
            results = re.findall('(?=(one|two|three|four|five|six|seven|eight|nine|zero|[0-9]))', line)
            number1 = get_number(results[0])
            number2 = get_number(results[-1])
            count = count + (number1 * 10 + number2)
        else:
            print(count)
            break


def get_number(data):
    if len(data) == 1:
        return int(data)
    match data:
        case 'one': return 1
        case 'two': return 2
        case 'three': return 3
        case 'four': return 4
        case 'five': return 5
        case 'six': return 6
        case 'seven': return 7
        case 'eight': return 8
        case 'nine': return 9


solve_puzzle2()
