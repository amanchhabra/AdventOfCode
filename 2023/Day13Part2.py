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




def toggle(str):
    if str == '.':
        return '#'
    else: return '.'

t = 0
test = []
for T in L:
    m = T.split("\n")
    found = False
    oans1 = find(m)
    na = [[n for n in node] for node in m]
    na = list(zip(*na))
    na = [''.join(n) for n in na]
    oans2 = find(na)
    for i in range(len(m)):
        for j in range(len(m[i])):
             if not found:
                m[i] = m[i][:j]+toggle(m[i][j])+m[i][j+1:]
                ans1 = find(m)
                na = [[n for n in node] for node in m]
                na = list(zip(*na))
                na = [''.join(n) for n in na]
                ans2 = find(na)

                if (len(ans1) > 0 or len(ans2) > 0) and (ans1 != oans1 or ans2 != oans2):
                    if len(ans1) > 0 and ans1 != oans1:
                        ans1 = [a for a in ans1 if a not in oans1]
                        t = t + (ans1[0])
                    if len(ans2) > 0 and ans2 != oans2:
                        ans2 = [a for a in ans2 if a not in oans2]
                        t = t + (100*ans2[0])
                    found = True
                m[i] = m[i][:j]+toggle(m[i][j])+m[i][j+1:]
print(t)

