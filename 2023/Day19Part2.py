import time
import sys
import re

workflows = {}
ratings = []
conditions = []


def check_only_rule(workflow, condition):
    global workflows
    global conditions
    if workflow == 'A':
        conditions.append(condition)
        return True
    elif workflow == 'R':
        return False
    another_condition = ''
    for rule in workflows[workflow].split(','):
        r_detail = rule.split(':')
        if len(r_detail) == 1:
            check_only_rule(r_detail[0], condition + another_condition)
        else:
            check_only_rule(r_detail[1], condition + another_condition + r_detail[0] + ',')
            conditiondetail = re.search('(\w)(.)(\d+)', r_detail[0])
            if conditiondetail.group(2) == '<':
                newcondition = conditiondetail.group(1) + '>' + str(int(conditiondetail.group(3)) - 1)
            else:
                newcondition = conditiondetail.group(1) + '<' + str(int(conditiondetail.group(3)) + 1)
            another_condition = another_condition + newcondition + ','


def main():
    D = open(sys.argv[1]).read().strip()
    W, R = D.split('\n\n')
    for line in R.split('\n'):
        LR = re.findall('\w+=\d+', line)
        rating = {a.split('=')[0]: int(a.split('=')[1]) for a in LR}
        ratings.append(rating)
    for line in W.split('\n'):
        a, b = re.search('(\w+){(.*)}', line).groups()
        workflows[a] = b
    t = 0
    check_only_rule('in', '')
    for condition in conditions:
        rating = {'x': list(range(1, 4001)), 'm': list(range(1, 4001)), 'a': list(range(1, 4001)), 's': list(range(1, 4001))}
        for current_condition in condition.split(','):
            if current_condition.count('<') == 1:
                condition_split = current_condition.split('<')
                rating[condition_split[0]] = [n for n in rating[condition_split[0]] if
                                    n < int(condition_split[1])]
            elif current_condition.count('>') == 1:
                current_condition_split = current_condition.split('>')
                rating[current_condition_split[0]] = [n for n in rating[current_condition_split[0]] if
                                    n > int(current_condition_split[1])]
        t = t + (len(rating['x']) * len(rating['m']) * len(rating['a']) * len(rating['s']))
    print(t)


if __name__ == '__main__':
    prev_time = time.perf_counter()
    main()
    done_time = time.perf_counter()
    print(f'Program completed in {done_time - prev_time:2f}s')
