import re


# Puzzle 1
def solve_puzzle1():
    second_attempt = False
    while True:
        line = input()

        # seeds
        seeds = [int(seed) for seed in re.findall("\d+", line)]
        data = []
        while True:
            line = input()
            if line:
                second_attempt = False
                if len(re.findall("\d+", line)) != 0:
                    data.append([int(soil) for soil in re.findall("\d+", line)])

            else:
                if second_attempt:
                    break
                else:
                    for i in range(len(seeds)):
                        for converter in data:
                            if converter[1] <= seeds[i] <= (converter[1] + converter[2]):
                                seeds[i] = converter[0] + (seeds[i] - converter[1])
                                break
                    second_attempt = True
                    data = []
        seeds.sort()
        print(seeds[0])
        break


# Puzzle 2
def solve_puzzle2():
    second_attempt = False
    while True:
        line = input()

        # seeds
        input_list = [int(seed) for seed in re.findall("\d+", line)]
        seeds = []
        for i in range(len(input_list)):
            if i % 2 == 0:
                seeds.append([input_list[i], input_list[i + 1]])

        data = []

        while True:
            line = input()
            if line:
                second_attempt = False
                if len(re.findall("\d+", line)) != 0:
                    data.append([int(soil) for soil in re.findall("\d+", line)])

            else:
                if second_attempt:
                    break
                elif len(data) > 0:
                    new_data = []
                    data.sort(key=sort_second)
                    print(data)
                    print(seeds)
                    print("till here")
                    while len(seeds) != 0:
                        seeds.sort(key=sort_first)
                        converted = False
                        for converter in data:
                            if converter[1] > seeds[0][0]:
                                converted = True
                                diff = converter[1] - seeds[0][0]
                                if diff >= seeds[0][1]:
                                    new_data.append(seeds[0])
                                    seeds.pop(0)
                                else:
                                    new_data.append([seeds[0][0], diff])
                                    seeds.append([seeds[0][0] + diff, seeds[0][1] - diff])
                                    seeds.pop(0)
                                break
                            elif converter[1] <= seeds[0][0] < (converter[1] + converter[2]):
                                converted = True
                                diff = converter[2] - (seeds[0][0] - converter[1])
                                if diff >= seeds[0][1]:
                                    new_data.append([seeds[0][0] - converter[1] + converter[0], seeds[0][1]])
                                    seeds.pop(0)
                                else:
                                    new_data.append([seeds[0][0] - converter[1] + converter[0], diff])
                                    seeds.append([seeds[0][0] + diff, seeds[0][1] - diff])
                                    seeds.pop(0)
                                break
                        if not converted:
                            new_data.append(seeds[0])
                            seeds.pop(0)

                    if len(new_data) != 0:
                        seeds = new_data
                    second_attempt = True
                    data = []
        seeds.sort(key=sort_first)
        print(seeds[0][0])
        break


def sort_second(val):
    return val[1]


def sort_first(val):
    return val[0]


solve_puzzle2()
