import time
import sys
import re
from collections import deque

dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def main():
    D = open(sys.argv[1]).read().strip()
    L = D.split('\n')
    m = [[n for n in node] for node in L]
    si, sj = 0, 0
    for i in range(len(m)):
        for j in range(len(m)):
            if m[i][j] == 'S':
                si, sj = i, j

    m[si][sj] = 'O'
    Q = deque()
    Q.append((si, sj, 0))

    SEEN = []
    EVEN_SEEN = set()
    ODD_SEEN = set()
    while Q:
        i, j, d = Q.popleft()
        if 0 <= i < len(m) and 0 <= j < len(m[0]) and m[i][j] != '#' and d < 65:
            m[i][j] = 'O'
            if (d % 2 == 0):
                EVEN_SEEN.add((i, j))
            else:
                ODD_SEEN.add((i, j))
            for ii, jj in dir:
                if 0 <= i + ii < len(m) and 0 <= j + jj < len(m[0]) and m[i + ii][j + jj] == 'O':
                    m[i + ii][j + jj] = '.'
                if (i + ii, j + jj, d + 1) not in SEEN and (i + ii, j + jj) not in EVEN_SEEN and (
                i + ii, j + jj) not in ODD_SEEN:
                    Q.append((i + ii, j + jj, d + 1))
                    SEEN.append((i + ii, j + jj, d + 1))

    t = 0
    for i in m:
        for j in i:
            if j == 'O':
                t += 1
    print(len(EVEN_SEEN))


if __name__ == '__main__':
    prev_time = time.perf_counter()
    main()
    done_time = time.perf_counter()
    print(f'Program completed in {done_time - prev_time:2f}s')
