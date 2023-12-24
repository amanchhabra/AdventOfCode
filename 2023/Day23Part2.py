import sys
from collections import deque
import time

dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
D = open(sys.argv[1]).read().strip()
L = D.split('\n')
m = [[n for n in node] for node in L]
h = len(m)
w = len(m[0])
si, sj = 0, 0
ti, tj = 0, 0
SEEN = []
max = 0
D = {}
nodes = {}


class Node:
    i, j = 0, 0
    connectingNode = {}
    seen = False

    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.connectingNode = {}
        self.seen = False

    def print(self):
        print(f'I am the node at {(self.i, self.j)})')

    def printConnectingNodes(self):
        print('Connecting Nodes')
        for node in self.connectingNode:
            node.print()
            print('is at distance')
            print(self.connectingNode[node])
        print()


def identifyNode(i, j, d, prevNode):
    S1 = []
    SEEN.append(prevNode)
    S1.append((prevNode.i, prevNode.j))
    t = True
    while t:
        S1.append((i, j))
        n = []
        for ii, jj in dir:
            if 0 <= i + ii < h and 0 <= j + jj < w and (i + ii, j + jj) not in S1 and m[i + ii][j + jj] != '#':
                n.append((i + ii, j + jj))

        if len(n) == 1:
            i, j = n[0]
            d += 1
        else:
            t = False
            if (i, j) not in nodes.keys():
                newnode = Node(i, j)
                nodes[(i, j)] = newnode
            newnode = nodes[(i, j)]
            if newnode not in prevNode.connectingNode:
                prevNode.connectingNode[newnode] = d
            if prevNode not in newnode.connectingNode:
                newnode.connectingNode[prevNode] = d
            if (i, j) not in nodes.keys() or nodes[(i, j)] not in SEEN:
                for i1, j1 in n:
                    identifyNode(i1, j1, 1, newnode)


def calcualteMaxNode(prevNode, d):
    global max
    if prevNode == nodes[(ti, tj)]:
        if d > max:
            max = d
    else:
        prevNode.seen = True
        for node in prevNode.connectingNode:
            if not node.seen:
                calcualteMaxNode(node, d + prevNode.connectingNode[node])
        prevNode.seen = False


def main():
    global si, sj, ti, tj, max
    for i in range(w):
        if m[0][i] == '.':
            si, sj = 0, i
    for i in range(w):
        if m[h - 1][i] == '.':
            ti, tj = h - 1, i
    Q = deque()
    D = {}
    Q.append((si, sj, 0, [], {}))
    y = 0
    for i in range(h):
        for j in range(w):
            if m[i][j] in ['^', '>', 'v', '<']:
                m[i][j] = '.'
            if m[i][j] == '.':
                y += 1
    if (si, sj) not in nodes.keys():
        node = Node(si, sj)
    nodes[(si, sj)] = node
    node = nodes[(si, sj)]
    identifyNode(si, sj, 0, node)
    calcualteMaxNode(node, 0)
    print(max)


if __name__ == '__main__':
    prev_time = time.perf_counter()
    main()
    done_time = time.perf_counter()
    print(f'Program completed in {done_time - prev_time:2f}s')
