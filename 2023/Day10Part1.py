import re
import sys

D = open(sys.argv[1]).read().strip()
L = D.split("\n")

m = [[n for n in line] for line in L]
si = 0
sj = 0
for i, v in enumerate(m):
    for j, vj in enumerate(v):
        if vj == 'S':
            si = i
            sj = j

# Up Right Down Left
dr = [-1, 0 , 1, 0]
dc = [0, 1, 0 , -1]

# direction
UP = 0
RIGHT = 1
BOTTOM = 2
LEFT = 3
d = UP
s = 'S'
if m[si+dr[UP]][sj+dc[UP]] in ['|', 'F', '7'] and m[si+dr[BOTTOM]][sj+dc[BOTTOM]] in ['|', 'L', 'J']:
    s = '|'
    d = UP
elif m[si+dr[LEFT]][sj+dc[LEFT]] in ['-', 'F', 'L'] and m[si+dr[RIGHT]][sj+dc[RIGHT]] in ['-', 'J', '7']:
    s = '-'
    d = RIGHT
elif m[si+dr[UP]][sj+dc[UP]] in ['|', 'F', '7'] and m[si+dr[RIGHT]][sj+dc[RIGHT]] in ['-', 'J', '7']:
    s = 'L'
    d = RIGHT
elif m[si+dr[BOTTOM]][sj+dc[BOTTOM]] in ['|', 'L', 'J'] and m[si+dr[RIGHT]][sj+dc[RIGHT]] in ['-', 'J', '7']:
    s = 'F'
    d = RIGHT
elif m[si+dr[UP]][sj+dc[UP]] in ['|', 'F', '7'] and m[si+dr[LEFT]][sj+dc[LEFT]] in ['-', 'F', 'L']:
    s = 'J'
    d = UP
elif m[si+dr[LEFT]][sj+dc[LEFT]] in ['-', 'F', 'L'] and m[si+dr[BOTTOM]][sj+dc[BOTTOM]] in ['|', 'L', 'J']:
    s = '7'
    d = LEFT
i = si
j = sj
count = 0
while True:
    print(m[i][j])
    count = count + 1
    i = i + dr[d]
    j = j + dc[d]
    if m[i][j] == 'L':
        if d == BOTTOM:
            d = RIGHT
        elif d == LEFT:
            d = UP
    if m[i][j] == 'J':
        if d == BOTTOM:
            d = LEFT
        elif d == RIGHT:
            d = UP
    if m[i][j] == 'F':
        if d == LEFT:
            d = BOTTOM
        elif d == UP:
            d = RIGHT
    if m[i][j] == '7':
        if d == RIGHT:
            d = BOTTOM
        elif d == UP:
            d = LEFT

    if i == si and j == sj:
        print(count // 2)
        break


