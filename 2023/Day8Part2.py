import math
import sys
import re
from collections import defaultdict, Counter
import functools


class Node:
    node = None
    left = ""
    right = ""


D = open(sys.argv[1]).read().strip()
L = D.split("\n")

c = L[0]

nodes = defaultdict(lambda: "Not Available")
for row in L[2:]:
    node = row.split(" = ")[0]
    left = row.split(" = ")[1].split(", ")[0][1:]
    right = row.split(" = ")[1].split(", ")[1][:3]
    nodes[node] = [left, right]
validNodes = [node for node in nodes.keys() if node[2:] == 'A']
maxCount = len(validNodes)
currentNode = "AAA"
totalCount = 0
for node in validNodes:
    counter = 0
    currentNode = node
    while(not currentNode.endswith("Z")):
        for command in c:
            counter = counter + 1
            match command:
                case 'L':
                        currentNode = nodes[currentNode][0]
                case 'R':
                        currentNode = nodes[currentNode][1]
    if totalCount == 0:
        totalCount = counter
    else:
        totalCount = totalCount * counter // math.gcd(totalCount, counter)
print(totalCount)