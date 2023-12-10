import re
import sys
import time
import os
from collections import deque

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
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# direction
UP = 0
RIGHT = 1
BOTTOM = 2
LEFT = 3
d = UP
s = 'S'
if m[si + dr[UP]][sj + dc[UP]] in ['|', 'F', '7'] and m[si + dr[BOTTOM]][sj + dc[BOTTOM]] in ['|', 'L', 'J']:
    s = '|'
    d = UP
elif m[si + dr[LEFT]][sj + dc[LEFT]] in ['-', 'F', 'L'] and m[si + dr[RIGHT]][sj + dc[RIGHT]] in ['-', 'J', '7']:
    s = '-'
    d = RIGHT
elif m[si + dr[UP]][sj + dc[UP]] in ['|', 'F', '7'] and m[si + dr[RIGHT]][sj + dc[RIGHT]] in ['-', 'J', '7']:
    s = 'L'
    d = RIGHT
elif m[si + dr[BOTTOM]][sj + dc[BOTTOM]] in ['|', 'L', 'J'] and m[si + dr[RIGHT]][sj + dc[RIGHT]] in ['-', 'J', '7']:
    s = 'F'
    d = RIGHT
elif m[si + dr[UP]][sj + dc[UP]] in ['|', 'F', '7'] and m[si + dr[LEFT]][sj + dc[LEFT]] in ['-', 'F', 'L']:
    s = 'J'
    d = UP
elif m[si + dr[LEFT]][sj + dc[LEFT]] in ['-', 'F', 'L'] and m[si + dr[BOTTOM]][sj + dc[BOTTOM]] in ['|', 'L', 'J']:
    s = '7'
    d = LEFT
m[si][sj] = s
i = si
j = sj
count = 0
arr = []
while True:
    arr.append([i, j])
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
F = ["...",
     ".##",
     ".#."]
S = ["...",
     "##.",
     ".#."]
L = [".#.",
     ".##",
     "..."]
J = [".#.",
     "##.",
     "..."]
P = [".#.",
     ".#.",
     ".#."]
D = ["...",
     "###",
     "..."]
e_arr = []


def expand(arr):
    for i, v in enumerate(m):
        for t in range(3):
            e_arr.append("")
            for j, vj in enumerate(v):
                if [i, j] in arr:
                    match vj:
                        case 'L':
                            e_arr[i * 3 + t] = e_arr[i * 3 + t] + L[t]
                        case 'F':
                            e_arr[i * 3 + t] = e_arr[i * 3 + t] + F[t]
                        case '7':
                            e_arr[i * 3 + t] = e_arr[i * 3 + t] + S[t]
                        case 'J':
                            e_arr[i * 3 + t] = e_arr[i * 3 + t] + J[t]
                        case '|':
                            e_arr[i * 3 + t] = e_arr[i * 3 + t] + P[t]
                        case '-':
                            e_arr[i * 3 + t] = e_arr[i * 3 + t] + D[t]
                else:
                    e_arr[i * 3 + t] = e_arr[i * 3 + t] + "..."


def printScreen(arr):
    count = 0
    os.system('clear')
    cnt = 0
    for i, v in enumerate(arr):
        ins = False
        for j, vj in enumerate(v):
            print(vj, end="")
        print()


expand(arr)
e_arr = [[n for n in node] for node in e_arr]

Q = deque()
Q.append((0, 0))
v = set()
while Q:
    r, c = Q.popleft()
    e_arr[r][c] = ' '
    for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(e_arr) and (0 <= nc < len(e_arr[0])) and (nr, nc) not in v and e_arr[nr][nc] == '.':
            Q.append((nr, nc))
            v.add((nr, nc))

    count = 0

for i in range(len(m)):
    for j in range(len(m[0])):
        valid = True
        for vi in range(3):
            for vj in range(3):
                if e_arr[i * 3 + vi][j * 3 + vj] != '.':
                    valid = False
        if valid:
            count = count + 1

print(count)