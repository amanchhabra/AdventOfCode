
def solve_puzzle1():
    line = input()
    for i in range(len(line)):
        if(i<3): pass
        else:
            data =  set([char for char in line[i-3:i+1]])
            if(len(data) == 4):
                print(f'The max count is {i+1}')
                break;

def solve_puzzle2():
    line = input()
    for i in range(len(line)):
        if(i<13): pass
        else:
            data =  set([char for char in line[i-13:i+1]])
            if(len(data) == 14):
                print(f'The max count is {i+1}')
                break;

solve_puzzle2()