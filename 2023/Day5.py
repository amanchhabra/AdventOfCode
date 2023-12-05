import re

# Puzzle 1

def solvePuzzle1() :
  count = 0
  secondattempt = False
  while (True):
      line = input()

      # seeds
      seeds = [int(seed) for seed in re.findall("\d+", line)]
      data = []
      while True:
          line = input()
          if line:
              secondattempt = False;
              if len(re.findall("\d+", line))!=0:
                  data.append([int(soil) for soil in re.findall("\d+", line)])

          else:
              if secondattempt:
                  break
              else:
                  for i in range(len(seeds)):
                      for converter in data:
                          if converter[1] <= seeds[i] <= (converter[1] + converter[2]):
                              seeds[i] = converter[0]+(seeds[i]-converter[1])
                              break
                  secondattempt = True
                  data = []
      seeds.sort()
      print(seeds[0])
      break





# Puzzle 2

def solvePuzzle2() :
    print([i for i in range(1,6)])
    count = 0
    secondattempt = False
    while (True):
        line = input()

        # seeds
        inputList = [int(seed) for seed in re.findall("\d+", line)]
        seeds = []
        for i in range(len(inputList)):
            if i%2==0:
                seeds.append([inputList[i], inputList[i+1]])

        data = []

        while True:
            line = input()
            if line:
                secondattempt = False;
                if len(re.findall("\d+", line))!=0:
                    data.append([int(soil) for soil in re.findall("\d+", line)])

            else:
                if secondattempt:
                    break
                elif len(data) > 0:
                    newdata = []
                    data.sort(key=sortSecond)
                    print(data)
                    print(seeds)
                    print("till here")
                    allConverted = False
                    while len(seeds) != 0:
                        seeds.sort(key=sortFirst)
                        converted = False;
                        for converter in data:
                            if converter[1]>seeds[0][0]:
                                converted = True
                                diff = converter[1]-seeds[0][0]
                                if diff >= seeds[0][1]:
                                    newdata.append(seeds[0])
                                    seeds.pop(0)
                                else:
                                    newdata.append([seeds[0][0], diff])
                                    seeds.append([seeds[0][0]+diff, seeds[0][1]-diff])
                                    seeds.pop(0)
                                break;
                            elif converter[1] <= seeds[0][0] < (converter[1] + converter[2]):
                                converted = True
                                diff = converter[2]-(seeds[0][0]-converter[1])
                                if diff >= seeds[0][1]:
                                    newdata.append([seeds[0][0]-converter[1]+converter[0], seeds[0][1]])
                                    seeds.pop(0)
                                else:
                                    newdata.append([seeds[0][0]-converter[1]+converter[0], diff])
                                    seeds.append([seeds[0][0]+diff, seeds[0][1]-diff])
                                    seeds.pop(0)
                                break
                        if not converted:
                           newdata.append(seeds[0])
                           seeds.pop(0)



                    if len(newdata) != 0 :
                        seeds = newdata
                    secondattempt = True
                    data = []
        seeds.sort(key=sortFirst)
        print(seeds[0][0])
        # print(seeds[0])
        break

def sortSecond(val):
    return val[1]

def sortFirst(val):
    return val[0]

solvePuzzle2()