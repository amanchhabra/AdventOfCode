import functools
import sys

D = open(sys.argv[1]).read().strip()
L = D.split("\n")
ans = 0


def simply_cards(data):
    return [13 if j == 'K' else 12 if j == 'Q' else 1 if j == 'J' else 10 if j == 'T' else 14 if j == 'A' else int(j)
            for j in data]


def compare_cards(data, data1):
    nsc = simply_cards(data[0])
    nsc1 = simply_cards(data1[0])
    if nsc[0] > nsc1[0]:
        return 1
    elif nsc[0] < nsc1[0]:
        return -1
    elif nsc[1] > nsc1[1]:
        return 1
    elif nsc[1] < nsc1[1]:
        return -1
    elif nsc[2] > nsc1[2]:
        return 1
    elif nsc[2] < nsc1[2]:
        return -1
    elif nsc[3] > nsc1[3]:
        return 1
    elif nsc[3] < nsc1[3]:
        return -1
    elif nsc[4] > nsc1[4]:
        return 1
    elif nsc[4] < nsc1[4]:
        return -1
    else:
        return 0


def sort_card(data, data1):
    if rank(data) > rank(data1):
        return 1
    elif rank(data) < rank(data1):
        return -1
    else:
        return compare_cards(data, data1)


def rank(data):
    sc = simply_cards(data[0])
    sc.sort()
    prev = -1
    repeat_count = []
    for j in sc:
        if j == prev and j != 1:
            repeat_count[-1] = repeat_count[-1] + 1
        else:
            prev = j
            repeat_count.append(1)
    repeat_count.sort(reverse=True)
    if sc.count(1) != 5:
        repeat_count[0] = repeat_count[0] + sc.count(1)
    else:
        repeat_count[0] = 5
    if repeat_count[0] >= 5:
        return 6
    elif repeat_count[0] == 4:
        return 5
    elif repeat_count[0] == 3:
        if repeat_count[1] == 2:
            return 4
        else:
            return 3
    elif repeat_count[0] == 2:
        if repeat_count[1] == 2:
            return 2
        else:
            return 1
    else:
        return 0


c = [cards.split() for cards in L]
c.sort(key=functools.cmp_to_key(sort_card))
count = 0
for i in range(len(c)):
    count = count + int(c[i][1]) * (i + 1)
print(count)
