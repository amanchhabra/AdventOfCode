import re

lines = []
stackdata = [[]]

# Read Stacks
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        stacks = [data for data in lines[-1].split(" ") if data != '']
        stackdata = [[stack[lines[-1].index(data)] for stack in lines if stack[lines[-1].index(data)] != '' and stack[lines[-1].index(data)] != ' ' and stack[lines[-1].index(data)] != data] for data in stacks]
        stackdata = [data[::-1] for data in stackdata]
        break

# Read instructions
def solve_puzzle1():
    while True:
        line = input()
        if line:
            results = re.search("move (\d*) from (\d*) to (\d*)", line)
            for x in range(int(results.group(1))):
                stackdata[int(results.group(3))-1].append(stackdata[int(results.group(2))-1].pop())
        else:
            result = ''.join([item[-1] for item in stackdata])
            print(f'The max count is {result}')
            break


def solve_puzzle2():
    while True:
        line = input()
        if line:
            results = re.search("move (\d*) from (\d*) to (\d*)", line)
            data = []
            for x in range(int(results.group(1))):
                data.append(stackdata[int(results.group(2))-1].pop())
            for x in range(len(data)):
                stackdata[int(results.group(3))-1].append(data.pop())
        else:
            result = ''.join([item[-1] for item in stackdata])
            print(f'The max count is {result}')
            break

solve_puzzle2()