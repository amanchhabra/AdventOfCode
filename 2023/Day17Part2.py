import sys
import heapq


D = open(sys.argv[1]).read().strip()
L = D.split("\n")
m = [[int(n) for n in node] for node in L]
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def f(loss, i, j, d, depth):
    global m
    D = {}
    Q = [(loss, i, j, d, depth)]
    while Q:
        loss, i, j, d, depth = heapq.heappop(Q)
        if (i,j, d, depth) in D:
            continue
        D[(i, j, d, depth)] = loss
        for d1, (ii, jj) in enumerate(dir):
            if (d1 + 2) % 4 != d:
                newd = depth + 1 if d1 == d else 1
                if (newd <= 10 and d1 == d) or (newd <= 10 and depth >= 4) or depth == -1:
                    if 0 <= i+ii < len(m) and 0 <= j+jj < len(m[0]):
                        if (i+ii, j+jj, d1, newd) in D:
                            continue
                        heapq.heappush(Q, (loss+m[i+ii][j+jj], i+ii, j+jj, d1, newd))
    t = 0
    for i, j, d, depth in D.keys():
        if i == len(m)-1 and j == len(m[0])-1:
            if t == 0 and depth >= 4:
                t = D[(i, j, d, depth)]
            t = min(t, D[(i, j, d, depth)])
    print(t)


f(0, 0, 0, -1, -1)
