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
g = []
for i, v in enumerate(m):
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
            nor = [i for i in o_r if (g1i < i < g2i or g2i < i < g1i)]
            noc = [j for j in oc if (g1j < j < g2j or g2j < j < g1j)]
            dist = abs(g1i-g2i)+abs(g1j-g2j)+999999*(len(nor)) + 999999*len(noc)
            count = count + dist
print(count//2)
