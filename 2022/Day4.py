def containsFullRange(range1, range2):
    if(range1.start <= range2.start and range1.stop >= range2.stop): return True
    if(range2.start <= range1.start and range2.stop >= range1.stop): return True
    else: return False

def overlap(range1, range2):
    overlapList = [value for value in [*range1] if value in [*range2]]
    return len(overlapList) > 0

def solve_puzzle1():
    totalCount = 0
    while True:
        line = input()
        if line:
           ranges = line.split(",")
           range1 = ranges[0].split("-")
           range2 = ranges[1].split("-")
           if containsFullRange(range(int(range1[0]),int(range1[1])), range(int(range2[0]),int(range2[1]))):
               totalCount = totalCount + 1
        else:
            print(f'Total count is {totalCount}')
            break

def solve_puzzle2():
    totalCount = 0
    while True:
        line = input()
        if line:
            ranges = line.split(",")
            range1 = ranges[0].split("-")
            range2 = ranges[1].split("-")
            if overlap(range(int(range1[0]),int(range1[1])+1), range(int(range2[0]),int(range2[1])+1)):
                totalCount = totalCount + 1
        else:
            print(f'Total count is {totalCount}')
            break

solve_puzzle2()
