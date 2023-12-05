import re

# Puzzle 1

def solvePuzzle1() :
  count = 0
  while (True):
      line = input()
      if line:
          results = re.search('Card\s+(\d+): ([\d\s]+) \| ([\d\s]+)', line)
          winningnumbers = [int(data) for data in re.findall('\d+',results.group(2))]
          numbers = [int(data) for data in re.findall('\d+',results.group(3))]
          win = [number for number in numbers if number in winningnumbers]
          if (len(win)>0):
              count = count + 2**(len(win)-1)

      else:
          print(count)
          break;



# Puzzle 2
def solvePuzzle2() :
    count = 0
    inputs = []
    while (True):
        for i in range(300):
            inputs.append(0)
        line = input()
        if line:
            results = re.search('Card\s+(\d+): ([\d\s]+) \| ([\d\s]+)', line)

            winningnumbers = [int(data) for data in re.findall('\d+',results.group(2))]
            numbers = [int(data) for data in re.findall('\d+',results.group(3))]
            win = [number for number in numbers if number in winningnumbers]
            cardnumber = int(results.group(1))
            if (len(win)>0):
                inputs[cardnumber] = inputs[cardnumber] + 1
                for y in range(inputs[cardnumber]):
                    for x in range(len(win)):
                        inputs[x+cardnumber+1] = inputs[x+cardnumber+1] + 1

            else:
                inputs[cardnumber] = inputs[cardnumber] + 1



        else:
            for card in inputs:
                count = count + card
            print(count)
            break;


solvePuzzle2()