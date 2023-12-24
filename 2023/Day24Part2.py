import time
import sys
from sympy import *
from sympy.abc import x, y, z, a, b, c, d, e, u, v, w

D = open(sys.argv[1]).read().strip()
L = D.split('\n')
m = [[n.split(' @ ')[0].split(', '), n.split(' @ ')[1].split(', ')] for n in L]
R = len(m)


def main():
    eq = []
    for i in range(4):
        t = a
        match i:
            case 0:
                t = a
            case 1:
                t = b
            case 2:
                t = c
            case 3:
                t = d
            case 4:
                t = e
        x1, y1, z1 = simplify(m[i][0][0]), simplify(m[i][0][1]), simplify(m[i][0][2])
        vx1, vy1, vz1 = simplify(m[i][1][0]), simplify(m[i][1][1]), simplify(m[i][1][2])
        eq.append(x1 + vx1 * t - x - v * t)
        eq.append(y1 + vy1 * t - y - w * t)
        eq.append(z1 + vz1 * t - z - u * t)
    t = solve(eq)
    print(t[0][x] + t[0][y] + t[0][z])


if __name__ == '__main__':
    prev_time = time.perf_counter()
    main()
    done_time = time.perf_counter()
    print(f'Program completed in {done_time - prev_time:2f}s')
