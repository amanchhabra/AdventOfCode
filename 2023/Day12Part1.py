import sys
import re

def valid_string(str, arr):
    str_arr = re.findall('#+', str)
    if len(str_arr) != len(arr):
        return False
    # print(str)
    for i in range(len(arr)):
        if i >= len(str_arr) or len(str_arr[i]) != arr[i]:
            return False

    return True



D = open(sys.argv[1]).read().strip()

L = D.split("\n")

m = [[n for n in node.split(' ')[0]] for node in L]
n = [[int(a) for a in a.split(' ')[1].split(',')] for a in L]
ind = 0
li = 0
sum = 0
for i,v in enumerate(m):
    lst = []
    for j, jv in enumerate(v):
        if jv == '?':
            lst.append(j)

    count = 0
    for l in range(pow(2,len(lst))) :
        vc = v
        bin_a = str(bin(l))[2:]
        bin_a = '0'*(len(lst)-len(bin_a))+bin_a
        for j, jv in enumerate(bin_a):
            if jv == '0':
                vc[lst[j]] = '#'
            else:
                vc[lst[j]] = '.'


        if valid_string(''.join(vc),n[i]) :
            count = count + 1
    sum = sum + count
print(sum)


