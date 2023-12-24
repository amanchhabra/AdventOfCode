import time
import sys

dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]


class Brick:
    id = 0
    otherBrick = []
    dBrick = []
    support = []

    def __init__(self, fx, fy, fz, sx, sy, sz, id):
        self.fx = fx
        self.fy = fy
        self.fz = fz
        self.sx = sx
        self.sy = sy
        self.sz = sz
        self.id = id
        self.dBrick = []
        self.support = []
        self.otherBrick = []

    def print(self):
        print(f'I am the brick at ({self.fx, self.fy, self.fz}) - ({self.sx, self.sy, self.sz})')

    def print1(self):
        print(f'{self.fx, self.fy, self.fz} {self.sx, self.sy, self.sz} {self.id}')

    def fallBrick(self):
        p1 = True
        while (p1):
            if min(self.fz, self.sz) != 1:
                if len(self.otherBrick) > 0:
                    for brick in self.otherBrick:
                        if min(self.fz - 1, self.sz - 1) == max(brick.fz, brick.sz):
                            p1 = False

                if p1:
                    self.fz -= 1
                    self.sz -= 1
            else:
                p1 = False
        return False


def solvebyzaxis(brick):
    return min(brick.fz, brick.sz)


def main():
    D = open(sys.argv[1]).read().strip()
    L = D.split('\n')
    m = [[(int(x.split(',')[0]), int(x.split(',')[1]), int(x.split(',')[2])) for x in n.split('~')] for n in L]
    m1 = []
    for i in range(len(m)):
        fx, fy, fz = m[i][0]
        sx, sy, sz = m[i][1]
        m1.append(Brick(fx, fy, fz, sx, sy, sz, i))

    t = len(m)
    m1.sort(key=solvebyzaxis, reverse=True)
    for i in range(t):
        for j in range(i + 1, t):
            assert m1[i].fx <= m1[i].sx
            assert m1[j].fx <= m1[j].sx
            assert m1[i].fy <= m1[i].sy
            assert m1[j].fy <= m1[j].sy
            if len([x for x in list(range(m1[i].fx, m1[i].sx + 1)) if x in list(range(m1[j].fx, m1[j].sx + 1))]) > 0 and \
                    len([y for y in list(range(m1[i].fy, m1[i].sy + 1)) if
                         y in list(range(m1[j].fy, m1[j].sy + 1))]) > 0:
                m1[i].otherBrick.append(m1[j])
    m1.sort(key=solvebyzaxis, reverse=True)
    for i in range(t):
        m1[t - i - 1].fallBrick()

    for i in range(t):
        for j in range(t):
            if len([x for x in list(range(m1[i].fx, m1[i].sx + 1)) if x in list(range(m1[j].fx, m1[j].sx + 1))]) > 0 and \
                    len([y for y in list(range(m1[i].fy, m1[i].sy + 1)) if
                         y in list(range(m1[j].fy, m1[j].sy + 1))]) > 0:
                if max(m1[i].fz, m1[i].sz) + 1 == min(m1[j].fz, m1[j].sz):
                    m1[i].support.append(m1[j])
                    m1[j].dBrick.append(m1[i])
    s = set()
    for b in m1:
        if len(b.dBrick) != 1:
            for b1 in b.dBrick:
                s.add(b1)
    for b in m1:
        if len(b.dBrick) == 1:
            if b.dBrick[0] in s:
                s.remove(b.dBrick[0])
    for b in m1:
        if len(b.support) == 0:
            s.add(b)
    print(len(s))


if __name__ == '__main__':
    prev_time = time.perf_counter()
    main()
    done_time = time.perf_counter()
    print(f'Program completed in {done_time - prev_time:2f}s')
