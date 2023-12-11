import sys

D = open(sys.argv[1]).read().strip()

L = D.split("\n")

m = [[n for n in node] for node in L]

oc = [i for i, n in enumerate(m[0]) if n == '.']
o_r = []
for i, v in enumerate(m):
    nc = [i for i, n in enumerate(v) if n == '.' and i in oc]
    oc = nc
    if len([a for a in v if a != '.']) == 0:
        o_r.append(i)
nm = []
nr = ''.join(['.' for a in range(len(m[0])+len(oc))])
for i in range(len(m)):
    if i in o_r:
        nm.append(nr)
        nm.append(nr)
    else:
        nm.append(''.join([m[i][a] if a not in oc else '..' for a in range(len(m[i]))]))

g = []
for i, v in enumerate(nm):
    for j, jv in enumerate(v):
        if jv == '#':
            g.append((i, j))

count = 0
for g1 in g:
    for g2 in g:
        if g1 == g2:
            pass
        else:
            g1i, g1j = g1
            g2i, g2j = g2
            dist = abs(g1i-g2i)+abs(g1j-g2j)
            count = count + dist
print(count//2)
