import time
import sys
from collections import deque

dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
D = open(sys.argv[1]).read().strip()
L = D.split('\n')
m = [[n for n in node] for node in L]
h = len(m)
w = len(m[0])
SEEN = []


def main():
    for i in range(w):
        if m[0][i] == '.':
            si, sj = 0, i
    for i in range(w):
        if m[h - 1][i] == '.':
            ti, tj = h - 1, i
    Q = deque()
    D = {}
    Q.append((si, sj, 0, []))
    while Q:
        i, j, d, SEEN = Q.popleft()
        if 0 <= i < h and 0 <= j < w:
            SEEN.append((i, j))
            if (i, j) not in D.keys() or D[(i, j)] < d:
                D[(i, j)] = d
                for i1 in range(4):
                    ii, jj = dir[i1]
                    if 0 <= i + ii < h and 0 <= j + jj < w and m[i + ii][j + jj] != '#':
                        if m[i + ii][j + jj] == '.' \
                                or (m[i + ii][j + jj] == '^' and i1 == 0) \
                                or (m[i + ii][j + jj] == '>' and i1 == 1) \
                                or (m[i + ii][j + jj] == 'v' and i1 == 2) \
                                or (m[i + ii][j + jj] == '<' and i1 == 3):
                            if (i + ii, j + jj) not in SEEN:
                                Q.append((i + ii, j + jj, D[(i, j)] + 1, SEEN.copy()))

    print(D[(ti, tj)])


def printArray(SEEN):
    for i1 in range(h):
        print()
        for i2 in range(w):
            if (i1, i2) in SEEN:
                print('O', end='')
            else:
                print(m[i1][i2], end='')


if __name__ == '__main__':
    prev_time = time.perf_counter()
    main()
    done_time = time.perf_counter()
    print(f'Program completed in {done_time - prev_time:2f}s')
