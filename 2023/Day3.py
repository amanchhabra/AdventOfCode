import re

# Puzzle 1

def solvePuzzle1() :
    lines = []
    count = 0
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    pointer = 0
    for line in lines:
        results = [(m.start(0), m.end(0), m.group(0)) for m in re.finditer("\d+", line)]
        for result in results:
            isValidPart = False
            if pointer != 0:
                oldline = lines[pointer - 1]
                matchString = oldline[0 if result[0]==0 else result[0]-1 : len(line) if result[1] == len(line) else result[1]+1 : 1]
                if len(re.findall("^[\d\.]+$", matchString))==0:
                   isValidPart = True
            if pointer < len(lines)-1:
                oldline = lines[pointer + 1]
                matchString = oldline[0 if result[0]==0 else result[0]-1 : len(line) if result[1] == len(line) else result[1]+1 : 1]
                if len(re.findall("^[\d\.]+$", matchString))==0:
                  isValidPart = True
            matchString = line[0 if result[0]==0 else result[0]-1 : len(line) if result[1] == len(line) else result[1]+1 : 1]
            if len(re.findall("^[\d\.]+$", matchString))==0:
                isValidPart = True
            if isValidPart:
                print(result[2])
                count = count + int(result[2])
        pointer = pointer + 1
        print(count)



# Puzzle 2

def solvePuzzle2() :
    lines = []
    count = 0
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    pointer = 0
    for line in lines:
        results = [(m.start(0), m.end(0), m.group(0)) for m in re.finditer("\*", line)]
        # print(results)
        for result in results:
            matchingParts = []
            if pointer != 0:
                oldline = lines[pointer - 1]
                oldline[0 if result[0]==0 else result[0]-1 : len(line) if result[1] == len(line) else result[1]+1 : 1]
                partresults = [(m.start(0), m.end(0), m.group(0)) for m in re.finditer("\d+", oldline)]
                for part in partresults:
                    if isConnectingToStar(part, result):
                        matchingParts.append(part)
            if pointer < len(lines)-1:
                oldline = lines[pointer + 1]
                partresults = [(m.start(0), m.end(0), m.group(0)) for m in re.finditer("\d+", oldline)]
                for part in partresults:
                    if isConnectingToStar(part, result):
                        matchingParts.append(part)
            line[0 if result[0]==0 else result[0]-1 : len(line) if result[1] == len(line) else result[1]+1 : 1]
            partresults = [(m.start(0), m.end(0), m.group(0)) for m in re.finditer("\d+", line)]
            for part in partresults:
                if isConnectingToStar(part, result):
                    matchingParts.append(part)
            if len(matchingParts) == 2:
                print(matchingParts)
                count = count + (int(matchingParts[0][2])*int(matchingParts[1][2]))
        pointer = pointer + 1

        print(count)


def isConnectingToStar(part, star):
    if part[0]-1 <= star[0] and star[1] <= part[1]+1:
        return True
    else:
        return False


solvePuzzle2()