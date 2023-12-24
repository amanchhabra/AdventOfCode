import time
import sys
import re
from collections import deque

BROADCASTER = 1
FLIPFLOP = 2
CONJUNCTION = 3
UNKNOWN = 4
map = {}
def addNode(node):
    if node in map.keys():
        return map[node]
    else:
        newN = Node(node)
        map[node] = newN
        return newN

class Node:
    name = ''
    on = True
    nodes = []
    memory = {}
    type = 1 # broadcaster

    def __init__(self, name):
        self.name = name
        self.on = False
        self.nodes = []
        self.memory = {}
        self.type = 1

    def addConnectingNode(self, node):
        self.nodes.append(node)
        if node.type == CONJUNCTION:
            node.memory[self] = False

    def processSignal(self, high, callingNode):
        if self.type == BROADCASTER:
            return high
        elif self.type == FLIPFLOP:
            if high:
                return None
            else:
                self.on = not self.on
                if self.on:
                    return True
                else:
                    return False
        elif self.type == CONJUNCTION:
            self.memory[callingNode] = high
            if all(self.memory.values()):
                return False
            else:
                return True



    def printNode(self):
        print(self.name)
        for node in self.nodes:
            print(f'-----> {node.name}')

def processSignal():
    highCount = 0
    lowCount = 0
    for i in range(1000):
        broadcaster = addNode('broadcaster')
        Q = deque()
        Q.append((broadcaster,False, None))
        SEEN = []
        while Q:
            node, high, callingNode = Q.popleft()
            SEEN.append(callingNode)
            signal = node.processSignal(high, callingNode)
            if high:
                highCount = highCount + 1
            else:
                lowCount = lowCount + 1
            for secondNode in node.nodes:
                if signal != None:
                    Q.append((secondNode, signal, node))
    print(highCount * lowCount)

def main():
    D = open(sys.argv[1]).read().strip()
    L = D.split('\n')
    for line in L:
        i = line.split(' -> ')
        if i[0] == 'broadcaster':
            node = addNode(i[0])
            node.type = BROADCASTER
            for data in i[1].split(', '):
                node.addConnectingNode(addNode(data))
        elif i[0][:1] == '%':
            node = addNode(i[0][1:])
            node.type = FLIPFLOP
            for data in i[1].split(', '):
                node.addConnectingNode(addNode(data))
        elif i[0][:1] == '&':
            node = addNode(i[0][1:])
            node.type = CONJUNCTION
            for data in i[1].split(', '):
                node.addConnectingNode(addNode(data))

    for node in map.values():
        for connecting in node.nodes:
            if connecting.type == CONJUNCTION:
                connecting.memory[node] = False
    addNode('broadcaster').printNode()
    processSignal()





if __name__ == '__main__':
    prev_time = time.perf_counter()
    main()
    done_time = time.perf_counter()
    print(f'Program completed in {done_time-prev_time:2f}s')