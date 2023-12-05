map = []
def isVisibleFromLeft(i,j, diff):
    pointer = j-diff
    if pointer < 0: return diff, True
    if map[i][j] <= map[i][pointer]: return diff+1, False
    else: return isVisibleFromLeft(i,j,diff+1)

def isVisibleFromRight(i,j, diff):
    pointer = j+diff
    if pointer >= len(map): return diff, True
    if map[i][j] <= map[i][pointer]: return diff+1, False
    else: return isVisibleFromRight(i,j,diff+1)

def isVisibleFromTop(i,j, diff):
    pointer = i-diff
    if pointer < 0: return diff, True
    if map[i][j] <= map[pointer][j]: return diff+1, False
    else: return isVisibleFromTop(i,j,diff+1)

def isVisibleFromBottom(i,j, diff):
    pointer = i+diff
    if pointer >= len(map): return diff, True
    if map[i][j] <= map[pointer][j]: return diff+1, False
    else: return isVisibleFromBottom(i,j,diff+1)

while True:
    line = input()
    if line:
        map.append([int(height) for height in line])
    else: break

def solve_puzzle1():
    visibleTree = 0;
    for i in range(len(map)):
        for j in range(len(map)):
            diffT, isVisibleTop = isVisibleFromTop(i,j,1)
            diffB, isVisibleBottom = isVisibleFromBottom(i,j,1)
            diffL, isVisibleLeft = isVisibleFromLeft(i,j,1)
            diffR, isVisibleRight = isVisibleFromRight(i,j,1)
            if isVisibleTop or isVisibleBottom or isVisibleLeft or isVisibleRight:
                visibleTree = visibleTree + 1


    print(f'The max count is {visibleTree}')

def solve_puzzle2():
    visibleTree = 0;
    for i in range(len(map)):
        for j in range(len(map)):
            diffT, isVisibleTop = isVisibleFromTop(i,j,1)
            diffB, isVisibleBottom = isVisibleFromBottom(i,j,1)
            diffL, isVisibleLeft = isVisibleFromLeft(i,j,1)
            diffR, isVisibleRight = isVisibleFromRight(i,j,1)
            if isVisibleTop or isVisibleBottom or isVisibleLeft or isVisibleRight:
                score = (diffT - 1) * (diffB - 1) * (diffL - 1) * (diffR - 1)
                if visibleTree < score:
                    visibleTree = score

    print(f'The max count is {visibleTree}')

solve_puzzle2()

