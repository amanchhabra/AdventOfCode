import sys
from collections import deque

D = open(sys.argv[1]).read().strip()
L = D.split("\n")
arraySize = 700
m = []
ci, cj = arraySize//2, arraySize//2
# U R D L
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
for i in range(arraySize):
    m.append(['.' for n in list(range(arraySize))])
m[ci][cj] = '#'

for line in L:
    i = line.split(' ')
    ii, jj = 0,0
    match i[0]:
        case 'R':
            ii, jj = dir[1]
        case 'L':
            ii, jj = dir[3]
        case 'D':
            ii, jj = dir[2]
        case 'U':
            ii, jj = dir[0]
    for i in range(int(i[1])):
        ci = ci + ii
        cj = cj + jj
        m[ci][cj] = '#'
Q = deque()
Q.append((0,0))
while Q:
    i1, j1 = Q.popleft()
    if 0 <= i1 < arraySize and 0 <= j1 < arraySize and m[i1][j1] == '.':
        m[i1][j1] = 'G'
        for i2, j2 in dir:
            Q.append((i1+i2, j1+j2))

t = 0
for i in range(arraySize):
    for j in range(arraySize):
        if m[i][j] != 'G':
            t = t + 1

print(t)
