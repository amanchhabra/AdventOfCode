import sys

D = open(sys.argv[1]).read().strip()
L = D.split("\n")
# U R D L
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
m = []
new_rules = []


def shoelace(verticies):
    t = 0
    for i in range(len(verticies)-1):
        ii, jj = verticies[i]
        oi, oj = verticies[i+1]
        t += ii*oj - jj*oi
    return abs(t)//2


def calculateArea(rule):
    vertices = [(0, 0)]
    linearea = 0
    for value, d in rule:
        match d:
            case '0':
                ii, jj = dir[1]
            case '1':
                ii, jj = dir[2]
            case '3':
                ii, jj = dir[0]
            case '2':
                ii, jj = dir[3]
        oi, oj = vertices[-1]
        vertices.append((oi+(ii*value), oj+(jj*value)))
        linearea += value
    return shoelace(vertices)+linearea//2+1


for line in L:
    i = line.split(' ')
    new_rules.append((int(i[2][2:-2], 16), i[2][-2:-1]))
print(calculateArea(new_rules))
