import sys
import re


def valid_start(str,arr):
    index = str.index('?')
    str1 = str[:index]
    str_arr = re.findall('#+', str1)
    if len(str[index + 1:]) < sum(arr[len(str_arr) + 1:]):
        return False
    for i in range(len(str_arr)):
        if len(str_arr) > len(arr):
            return False
        if len(str_arr[i]) != arr[i] and i != len(str_arr)-1:
            return False
        if len(str_arr[i]) > arr[i]:
            return False
    return True

def valid_string(str, arr):
    str_arr = re.findall('#+', str)
    if len(str_arr) != len(arr):
        return False
    for i in range(len(arr)):
        if i >= len(str_arr) or len(str_arr[i]) != arr[i]:
            return False
    return True


def recur_possibilities(str, arr):
    if str.count('?') == 0:
        if valid_string(str, arr): return 1
        else: return 0
    if not valid_start(str, arr):
        return 0
    find = str.find('?')
    str1 = str[:find] + '.' + str[find + 1:]
    str2 = str[:find] + '#' + str[find + 1:]
    return recur_possibilities(str1, arr) + recur_possibilities(str2, arr)

D = open(sys.argv[1]).read().strip()

L = D.split("\n")
L = [n.split(" ")[0]+'?'+n.split(" ")[0]+'?'+n.split(" ")[0]+'?'+n.split(" ")[0]+'?'+n.split(" ")[0]+' '+n.split(" ")[1]+','+n.split(" ")[1]+','+n.split(" ")[1]+','+n.split(" ")[1]+','+n.split(" ")[1] for n in L]

m = [[n for n in node.split(' ')[0]] for node in L]
n = [[int(a) for a in a.split(' ')[1].split(',')] for a in L]

ind = 0
li = 0
total = 0
for i,v in enumerate(m):
    vt = ''.join(v)
    b = re.findall('#+.', vt[:vt.index('?')])
    count = recur_possibilities(''.join(v), n[i])
    total = total + count
print(total)

