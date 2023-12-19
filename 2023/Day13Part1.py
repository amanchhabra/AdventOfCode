import re
import sys

D = open(sys.argv[1]).read().strip()
L = D.split("\n\n")


def find(m):
    p = []
    a = m[0]
    for i in range(1, len(a)):
        if i < len(a) / 2:
            if a[i:].startswith(a[:i][::-1]):
                p.append(i)
        else:
            if a[:i][::-1].startswith(a[i:]):
                p.append(i)
    for i in range(len(m)):
        for j in range(len(m[0])):
            if j in p:
                if j < len(m[i]) / 2:
                    if not m[i][j:].startswith(m[i][:j][::-1]):
                        p.remove(j)
                else:
                    if not m[i][:j][::-1].startswith(m[i][j:]):
                        p.remove(j)
    return p



t = 0
test = []
for T in L:
    m = T.split("\n")
    ans = find(m)
    if(len(ans)>0):
        test.append(ans[0])
    t = t + sum(find(m))
    m = [[n for n in node] for node in m]
    m = list(zip(*m))
    m = [''.join(n) for n in m]
    ans = find(m)
    ans = [100*n for n in ans]
    t = t + sum(ans)
print(t)

