import re


# Puzzle 1
def solve_puzzle1():
    count = 0
    while True:
        line = input()
        if line:
            game_number = re.findall('\d+', line)[0]
            results = re.findall('(\d+)\s(blue|red|green)', line)
            game_possible = True
            for cube in results:
                match cube[1]:
                    case 'blue':
                        if int(cube[0]) > 14:
                            game_possible = False
                    case 'red':
                        if int(cube[0]) > 12:
                            game_possible = False
                    case 'green':
                        if int(cube[0]) > 13:
                            game_possible = False
            if game_possible:
                print(game_number)
                count = count + int(game_number)
            else:
                print(count)


# Puzzle 2
def solve_puzzle2():
    count = 0
    while True:
        line = input()
        if line:
            results = re.findall('(\d+)\s(blue|red|green)', line)
            red_count = 0
            blue_count = 0
            green_count = 0
            for cube in results:
                match cube[1]:
                    case 'blue':
                        if int(cube[0]) > blue_count:
                            blue_count = int(cube[0])
                    case 'red':
                        if int(cube[0]) > red_count:
                            red_count = int(cube[0])
                    case 'green':
                        if int(cube[0]) > green_count:
                            green_count = int(cube[0])
            game_power = red_count * green_count * blue_count
            count = count + game_power
        else:
            print(count)


solve_puzzle2()
