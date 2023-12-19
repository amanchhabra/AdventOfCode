import sys
import re
from collections import deque


def print_func(arr):
    for i in arr:
        print(''.join(i))

    print()

def change_array(arr):
    for i in range(len(arr)):
        arr[i] = [n for n in f(''.join(arr[i]))]

    return arr
def f(str):
    que = deque()
    for i in range(len(str)):
        if str[i] == '.':
            que.append(i)
        elif str[i] == 'O':
            if que:
                pos = que.popleft()
                str = str[:pos]+'O'+str[pos+1:i]+'.'+str[i+1:]
                que.append(i)
        elif str[i] == '#':
            que.clear()
    return str

D = open(sys.argv[1]).read().strip()

L = D.split("\n")

m = [[n for n in node ] for node in L]

oldm = m
dp = []
si = 0
ei = 0
matchdp = None
for i in range(1000000000):
    m = list(zip(*m))[::-1]
    m = change_array(m)
    m = list(zip(*m[::-1]))
    m = change_array(m)
    m = list(zip(*m[::-1]))
    m = change_array(m)
    m = list(zip(*m[::-1]))
    m = change_array(m)
    m = list(zip(*m[::-1]))
    m = list(zip(*m[::-1]))
    if m == matchdp:
        ei = i
        break
    if not matchdp and m in dp:
        si = i
        matchdp = m
    dp.append(m)
#

d = ei - si
r = (1000000000 - ei)%d
for i in range(r-1):
    m = list(zip(*m))[::-1]
    m = change_array(m)
    m = list(zip(*m[::-1]))
    m = change_array(m)
    m = list(zip(*m[::-1]))
    m = change_array(m)
    m = list(zip(*m[::-1]))
    m = change_array(m)
    m = list(zip(*m[::-1]))
    m = list(zip(*m[::-1]))
str = 'OO.O.O..##'

t = 0

for i in range(len(m)):
    t = t + ((len(m)-i)*'.'.join(m[i]).count('O'))

print(t)

