import sys
import re

D = open(sys.argv[1]).read().strip()

L = D.split("\n")

m = [[n for n in node.split(' ')[0]] for node in L]
n = [[0 for a in node] for node in m]
sys.setrecursionlimit(10000)
LEFT = 1
RIGHT = 2
BOTTOM = 3
TOP = 4


DP = []
def f(i,j, dir):
    global m
    global n
    if not 0 <= i < len(m) or not 0<= j < len(m[0]):
        return
    if (i,j,dir) in DP:
        return
    DP.append((i,j,dir))
    n[i][j] = n[i][j] + 1
    match m[i][j]:
        case '|':
            if dir == LEFT or dir == RIGHT:
                f(i-1,j,TOP)
                f(i+1,j,BOTTOM)
            elif dir == TOP:
                f(i-1,j,TOP)
            elif dir == BOTTOM:
                f(i+1,j,BOTTOM)
        case '-':
            if dir == TOP or dir == BOTTOM:
                f(i,j-1,LEFT)
                f(i,j+1,RIGHT)
            elif dir == LEFT:
                f(i,j-1,LEFT)
            elif dir == RIGHT:
                f(i,j+1,RIGHT)
        case '.':
            if dir == TOP:
                f(i-1,j,TOP)
            elif dir == BOTTOM:
                f(i+1,j,BOTTOM)
            elif dir == LEFT:
                f(i,j-1,LEFT)
            elif dir == RIGHT:
                f(i,j+1,RIGHT)
        case '/':
            if dir == BOTTOM:
                f(i,j-1,LEFT)
            elif dir == TOP:
                f(i,j+1,RIGHT)
            elif dir == RIGHT:
                f(i-1,j,TOP)
            elif dir == LEFT:
                f(i+1,j,BOTTOM)
        case '\\':
            if dir == TOP:
                f(i,j-1,LEFT)
            elif dir == BOTTOM:
                f(i,j+1,RIGHT)
            elif dir == LEFT:
                f(i-1,j,TOP)
            elif dir == RIGHT:
                f(i+1,j,BOTTOM)


def calc():
    global n
    t = 0
    for i in n:
        for j in i:
            if j > 0:
                t = t + 1

    return t
t = 0
for i in range(len(m)):
    f(i,0,RIGHT)
    nt = calc()
    t = nt if nt > t else t
    DP.clear()
    n = [[0 for a in node] for node in m]
    print(f'Done row {i} / {len(m)}  from right')

for i in range(len(m)):
    f(i,len(m[0])-1,LEFT)
    nt = calc()
    t = nt if nt > t else t
    DP.clear()
    n = [[0 for a in node] for node in m]
    print(f'Done row {i} / {len(m[0])}  from left')

for i in range(len(m[0])):
    f(0,i,BOTTOM)
    nt = calc()
    t = nt if nt > t else t
    DP.clear()
    n = [[0 for a in node] for node in m]
    print(f'Done col {i} / {len(m[0])} from bottom')


for i in range(len(m[0])):
    f(len(m)-1,i,TOP)
    nt = calc()
    t = nt if nt > t else t
    DP.clear()
    n = [[0 for a in node] for node in m]
    print(f'Done col {i} / {len(m[0])} from top')

print(t)

