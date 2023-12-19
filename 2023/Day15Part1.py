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

t = 0
for i in m:
    t = t+ func(i)
print(t)
