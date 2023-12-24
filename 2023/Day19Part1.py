import time
import sys
import re

workflows = {}
ratings = []
conditions = []


def check_rule(workflow, data):
    global workflows
    if workflow == 'A':
        return True
    elif workflow == 'R':
        return False
    for rule in workflows[workflow].split(','):
        r_detail = rule.split(':')
        if len(r_detail) == 1:
            return check_rule(r_detail[0], data)
        else:
            if r_detail[0].count('>') == 1:
                if data[r_detail[0].split('>')[0]] > int(r_detail[0].split('>')[1]):
                    return check_rule(r_detail[1], data)
            else:
                if data[r_detail[0].split('<')[0]] < int(r_detail[0].split('<')[1]):
                    return check_rule(r_detail[1], data)


def main():
    D = open(sys.argv[1]).read().strip()
    W, R = D.split('\n\n')
    for line in R.split('\n'):
        LR = re.findall('\w+=\d+', line)
        rating = {a.split('=')[0]:int(a.split('=')[1]) for a in LR}
        ratings.append(rating)
    for line in W.split('\n'):
        a,b = re.search('(\w+){(.*)}',line).groups()
        workflows[a] = b
    t = 0
    for rating in ratings:
        if check_rule('in', rating):
            for a in rating.values():
                t = t + a
    print(t)



if __name__ == '__main__':
    prev_time = time.perf_counter()
    main()
    done_time = time.perf_counter()
    print(f'Program completed in {done_time-prev_time:2f}s')