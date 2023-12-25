import time
import sys
from networkx import DiGraph, minimum_cut

D = open(sys.argv[1]).read().strip()
L = D.split('\n')
def main():
    t = set()
    g = DiGraph()
    w = []
    for line in L:
        a = line.split(': ')
        t.add(a[0])
        b = a[1].split(' ')
        for connectingnode in b:
            t.add(connectingnode)
            if (a[0],connectingnode) not in w and (connectingnode, a[0]) not in w:
                w.append((a[0],connectingnode))

        for x,y in w:
            g.add_edge(x,y,capacity=1.0)
            g.add_edge(y,x,capacity=1.0)
    for s in t:
        for t1 in t:
            if s != t1:
                cut, (a,b) = minimum_cut(g, t1, s)
                if cut == 3.0:
                   print(len(a) * len(b))
                   return




if __name__ == '__main__':
    prev_time = time.perf_counter()
    main()
    done_time = time.perf_counter()
    print(f'Program completed in {done_time - prev_time:2f}s')
