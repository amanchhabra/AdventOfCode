import time
import sys
from collections import deque

dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def solve(si, sj, mi, m):
    Q = deque()
    Q.append((si, sj, 0, 0, 0))
    SEEN = {}
    EVEN_SEEN = set()
    ODD_SEEN = set()
    while Q:
        i, j, ti, tj, d = Q.popleft()
        if i == -1:
            i = len(m) - 1
            ti -= 1
        if i == len(m):
            i = 0
            ti += 1
        if j == -1:
            j = len(m) - 1
            tj -= 1
        if j == len(m):
            j = 0
            tj += 1
        if m[i][j] != '#' and d < mi:
            if (d % 2 == 0):
                EVEN_SEEN.add((i, j, ti, tj))
            else:
                ODD_SEEN.add((i, j, ti, tj))
            for ii, jj in dir:
                if (i + ii, j + jj, ti, tj) not in SEEN and (i + ii, j + jj, ti, tj) not in EVEN_SEEN and (
                        i + ii, j + jj, ti, tj) not in ODD_SEEN:
                    Q.append((i + ii, j + jj, ti, tj, d + 1))
                    SEEN[(i + ii, j + jj, ti, tj)] = d + 1
    return EVEN_SEEN, ODD_SEEN


def main():
    D = open(sys.argv[1]).read().strip()
    L = D.split('\n')
    m = [[n for n in node] for node in L]
    si, sj = 0, 0
    for i in range(len(m)):
        for j in range(len(m)):
            if m[i][j] == 'S':
                si, sj = i, j

    gridSize = len(m)
    steps = 26501365 - gridSize // 2
    maxReach = steps // gridSize
    full_grid_even_seen, full_grid_odd_seen = solve(si, sj, gridSize // 2 + gridSize + gridSize + 1, m)
    corner_grid_even_seen, corned_grid_odd_seen = solve(si, sj, gridSize // 2 + gridSize + gridSize + 1, m)
    oddarea = ((maxReach - 1) ** 2) * sum(1 for a, b, c, d in full_grid_odd_seen if c == 0 and d == 0)
    oddarea += ((maxReach) ** 2) * sum(1 for a, b, c, d in full_grid_odd_seen if c == 0 and d == 1)
    oddarea += sum(1 for a, b, c, d in corned_grid_odd_seen if c == 0 and d == 2)
    oddarea += sum(1 for a, b, c, d in corned_grid_odd_seen if c == 2 and d == 0)
    oddarea += sum(1 for a, b, c, d in corned_grid_odd_seen if c == -2 and d == 0)
    oddarea += sum(1 for a, b, c, d in corned_grid_odd_seen if c == 0 and d == -2)
    oddarea += (maxReach - 1) * sum(1 for a, b, c, d in corned_grid_odd_seen if c == 1 and d == 1)
    oddarea += (maxReach - 1) * sum(1 for a, b, c, d in corned_grid_odd_seen if c == -1 and d == 1)
    oddarea += (maxReach - 1) * sum(1 for a, b, c, d in corned_grid_odd_seen if c == 1 and d == -1)
    oddarea += (maxReach - 1) * sum(1 for a, b, c, d in corned_grid_odd_seen if c == -1 and d == -1)
    oddarea += (maxReach) * sum(1 for a, b, c, d in corned_grid_odd_seen if c == 1 and d == 2)
    oddarea += (maxReach) * sum(1 for a, b, c, d in corned_grid_odd_seen if c == -2 and d == 1)
    oddarea += (maxReach) * sum(1 for a, b, c, d in corned_grid_odd_seen if c == 1 and d == -2)
    oddarea += (maxReach) * sum(1 for a, b, c, d in corned_grid_odd_seen if c == -2 and d == -1)
    print(oddarea)


if __name__ == '__main__':
    prev_time = time.perf_counter()
    main()
    done_time = time.perf_counter()
    print(f'Program completed in {done_time - prev_time:2f}s')
