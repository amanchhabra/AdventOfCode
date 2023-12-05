
def priority(a):
    return ord(a) - 96 if ord(a)> 96 else ord(a)-38

def findDuplicate(string1, string2):
    return list(set([i for i in string1+string2 if string1.count(i) > 0 and string2.count(i) > 0]))

def findDuplicate(string1, string2, string3):
    return list(set([i for i in string1 if string1.count(i) > 0 and string2.count(i) > 0 and string3.count(i) > 0]))




def solve_puzzle1():
    totalCount = 0
    while(True):
        line = input()
        if line:
            quotient, remainder = divmod(len(line), 2)
            duplicates = findDuplicate(line[:quotient + remainder],line[quotient + remainder:])
            for i in duplicates:
                totalCount = totalCount + priority(i)
        else:
            print(f'Max count is {totalCount}')
            break


def solve_puzzle2():
    totalCount = 0
    lineCount = 0
    lines = []
    while(True):
        line = input()
        if line:
            lineCount = lineCount + 1
            lines.append(line)
            if lineCount % 3 == 0:
                lineCount = 0
                duplicates = findDuplicate(lines[0], lines[1], lines[2])
                for i in duplicates:
                    totalCount = totalCount + priority(i)
                lines = []
        else:
            print(f'Max count is {totalCount}')
            break


solve_puzzle2()

