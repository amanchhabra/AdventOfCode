import re

# Puzzle 1

def solvePuzzle1() :
   line = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
   count = 0
   while True:
       line = input()
       if line:
           gamenumber = re.findall('\d+', line)[0]
           results = re.findall('(\d+)\s(blue|red|green)', line)
           redCount = 0
           blueCount = 0
           greenCount = 0
           gamePossible = True
           for cube in results:
               match cube[1]:
                   case 'blue':
                       if int(cube[0])>14:
                           gamePossible = False
                   case 'red':
                       if int(cube[0])>12:
                           gamePossible = False
                   case 'green':
                       if int(cube[0])>13:
                           gamePossible = False
               # match cube[1]:
               #     case 'blue': blueCount = blueCount + int(cube[0])
               #     case 'red': redCount = redCount + int(cube[0])
               #     case 'green': greenCount = greenCount + int(cube[0])

           if gamePossible:
               print(gamenumber)
               count = count + int(gamenumber)
       else:
           print(count)

# Puzzle 2
def solvePuzzle2() :
    line = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    count = 0
    while True:
        line = input()
        if line:
            gamenumber = re.findall('\d+', line)[0]
            results = re.findall('(\d+)\s(blue|red|green)', line)
            redCount = 0
            blueCount = 0
            greenCount = 0
            gamePossible = True
            for cube in results:
                match cube[1]:
                    case 'blue':
                        if int(cube[0])>blueCount:
                            blueCount = int(cube[0])
                    case 'red':
                        if int(cube[0])>redCount:
                           redCount = int(cube[0])
                    case 'green':
                        if int(cube[0])>greenCount:
                            greenCount = int(cube[0])
            gamePower = redCount * greenCount * blueCount
            count = count + gamePower
        else:
            print(count)
solvePuzzle2()