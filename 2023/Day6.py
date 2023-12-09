import re


# Puzzle 1
def solve_puzzle1():
    count = 0
    line = input()
    times = [int(time) for time in re.findall('\d+', line)]

    line = input()
    distances = [int(distance) for distance in re.findall('\d+', line)]

    for time in range(len(times)):
        ways = 0
        speed = 0
        for second in range(times[time]):
            if(speed*(times[time]-second)) > distances[time]:
                ways = ways+1
            speed = speed + 1
        if count == 0:
            count = ways
        else:
            count = count * ways
    print(count)


# Puzzle 2
def solve_puzzle2():
    count = 0
    line = input()
    times = [int("".join(re.findall('\d+', line)))]

    line = input()
    distances = [int("".join(re.findall('\d+', line)))]
    for time in range(len(times)):
        ways = 0
        speed = 0
        for second in range(times[time]):
            if(speed*(times[time]-second)) > distances[time]:
                ways = ways+1
            speed = speed + 1
        if count == 0:
            count = ways
        else:
            count = count * ways
    print(count)


solve_puzzle2()
