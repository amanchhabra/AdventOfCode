import sys
import re
from collections import deque


def print_func(arr):
    for i in arr:
        print(''.join(i))

    print()


def func(str):
    current = 0
    for i in str:
        current = current + ord(i)
        current = current * 17
        current = current % 256
    return current


D = open(sys.argv[1]).read().strip()

L = D.split(",")

m = [node for node in L]
j = []
for i in range(256):
    j.append([])

t = 0
for i in m:
    focal = t+func(i)
    if '=' in i:
        label = i[:i.index('=')]
        value = i[i.index('=')+1:]
        hash = func(label)
        found = False
        for c,v in enumerate(j[hash]):
            if v[0] == label:
                j[hash][c][1] = value
                found = True
                break
        if not found:
            j[hash].append([label,value])
    else:
        label = i[:i.index('-')]
        hash = func(label)
        for c,v in enumerate(j[hash]):
            if v[0] == label:
                j[hash].remove(v)
                break

for i in range(256):
    for i1 in range(len(j[i])):
        t = t + ((i+1) * (i1+1) * int(j[i][i1][1]))

print(t)


