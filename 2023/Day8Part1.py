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
    nodes[node]=[left,right]


currentNode = "AAA"
counter = 0
while currentNode!= "ZZZ":
    for command in c:
        counter = counter + 1
        match command:
            case 'L':
                currentNode = nodes[currentNode][0]
            case 'R':
                currentNode = nodes[currentNode][1]
print(counter)

