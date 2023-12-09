import sys
import re
from collections import defaultdict
import functools
D = open(sys.argv[1]).read().strip()
L = D.split("\n")
ans = 0

def simplyCards(data):
    return [13 if c == 'K' else 12 if c == 'Q' else 11 if c=='J' else 10 if c=='T' else 14 if c=='A' else int(c) for c in data]

def compareCards(data,data1):
    nsc = simplyCards(data[0])
    nsc1 = simplyCards(data1[0])
    if nsc[0] > nsc1[0]: return 1
    elif nsc[0] < nsc1[0]: return -1
    elif nsc[1] > nsc1[1]: return 1
    elif nsc[1] < nsc1[1]: return -1
    elif nsc[2] > nsc1[2]: return 1
    elif nsc[2] < nsc1[2]: return -1
    elif nsc[3] > nsc1[3]: return 1
    elif nsc[3] < nsc1[3]: return -1
    elif nsc[4] > nsc1[4]: return 1
    elif nsc[4] < nsc1[4]: return -1
    else: return 0



def sortCard(data, data1):
    if (rank(data)> rank(data1)):
        return 1
    elif (rank(data)< rank(data1)):
        return -1
    else:
        return compareCards(data,data1)

def rank(data):
    sc = simplyCards(data[0])
    sc.sort()
    prev = -1
    repeatCount = []
    for c in sc:
        if c == prev:
            repeatCount[-1] = repeatCount[-1]+1
        else :
            prev = c
            repeatCount.append(1)
    repeatCount.sort(reverse=True)
    if repeatCount[0] == 5:
        return 6
    elif repeatCount[0] == 4:
        return 5
    elif repeatCount[0] == 3:
        if repeatCount[1] == 2:
            return 4
        else:
            return 3
    elif repeatCount[0] == 2:
        if repeatCount[1] == 2:
            return 2
        else:
            return 1
    else:
        return 0


c = [cards.split() for cards in L]
c.sort(key=functools.cmp_to_key(sortCard))
count = 0
for i in range(len(c)):
    count = count + int(c[i][1])*(i+1)
print(count)
