import re
import sys

D = open(sys.argv[1]).read().strip()
L = D.split("\n")
o = []
for line in L:
    inp = [int(p) for p in re.findall('-?\d+', line)]
    inputs = []
    ni = inp
    while len([d for d in ni if d != 0]) != 0:
        nj = []
        for i, j in enumerate(ni):
            if i < len(ni) - 1:
                nj.append(ni[i + 1] - ni[i])
        inputs.append(nj)
        ni = nj
    inputs.reverse()
    prev = 0
    diff = 0
    for i, j in enumerate(inputs):
        if i > 0:
            diff = diff + j[-1]
    o.append(diff + inp[-1])
print(sum(o))
