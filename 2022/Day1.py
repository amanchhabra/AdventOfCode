

# Puzzle 1

def solvePuzzle1() :
    elfcount = 0
    maxcount = 0
    lines = []
    while True:
        line = input()
        if line:
            elfcount += int(line)
        else:
            maxcount = maxcount if maxcount > elfcount else elfcount
            if elfcount == 0:
                break
            elfcount = 0
    print(f"Max calories are {maxcount}")

    # Puzzle 1

def solvePuzzle2() :
    elfcount = 0
    maxcount = []
    while True:
        line = input()
        if line:
            elfcount += int(line)
        else:
            maxcount.append(elfcount)
            if elfcount == 0:
                break
            elfcount = 0

    maxcount.sort()
    totalCount = maxcount[-1] + maxcount[-2] + maxcount[-3]
    print(f"Max total calories are {totalCount}")


solvePuzzle2()