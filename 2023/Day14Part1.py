import sys
import re
from collections import deque


def print_func(arr):
    for i in arr:
        print(''.join(i))

    print()

def convert_array(arr):
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

m = [[n for n in node] for node in L]
m = list(zip(*m))
m = convert_array(m)
m = list(zip(*m))
t = 0

for i in range(len(m)):
    t = t + ((len(m)-i)*'.'.join(m[i]).count('O'))

print(t)

