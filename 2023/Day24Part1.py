import time
import sys
from sympy import solve, simplify
from sympy.abc import x, y

dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
D = open(sys.argv[1]).read().strip()
L = D.split('\n')
m = [[n.split(' @ ')[0].split(', '), n.split(' @ ')[1].split(', ')] for n in L]
R = len(m)


def main():
    m1, m2 = 200000000000000, 400000000000000
    t = 0
    SEEN = []
    for i in range(R):
        for j in range(R):
            if i != j and (i, j) not in SEEN and (j, i) not in SEEN:
                SEEN.append((i, j))
                x1, y1 = simplify(m[i][0][0]), simplify(m[i][0][1])
                x2, y2 = simplify(m[j][0][0]), simplify(m[j][0][1])
                vx1, vy1 = simplify(m[i][1][0]), simplify(m[i][1][1])
                vx2, vy2 = simplify(m[j][1][0]), simplify(m[j][1][1])
                time = solve([x1 + (vx1 * x) - (vx2 * y) - x2, y1 + (vy1 * x) - (vy2 * y) - y2])
                if len(time) == 2:
                    if time[x] >= 0 and time[y] >= 0 and m1 <= x1 + (vx1 * time[x]) <= m2 and m1 <= y1 + (
                            vy1 * time[x]) <= m2:
                        t = t + 1
    print(t)


if __name__ == '__main__':
    prev_time = time.perf_counter()
    main()
    done_time = time.perf_counter()
    print(f'Program completed in {done_time - prev_time:2f}s')
