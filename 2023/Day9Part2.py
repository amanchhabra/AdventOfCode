import sys
import re
from collections import defaultdict, Counter
import functools

D = open(sys.argv[1]).read().strip()
L = D.split("\n")
o = []
for line in L:
    input = [int(p) for p in re.findall('\-?\d+',line)]
    inputs = []
    ni = input
    while len([d for d in ni if d != 0]) != 0 :
        nj = []
        for i,j in enumerate(ni):
            if i < len(ni)-1:
                nj.append(ni[i+1]-ni[i])
        inputs.append(nj)
        ni = nj
    inputs.reverse()
    prev = 0
    diff = 0
    for i,j in enumerate(inputs):
        if i > 0:
            diff = j[0]-diff
    o.append(input[0]-diff)
print(sum(o))



