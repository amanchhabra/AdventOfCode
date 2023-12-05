class Dir:
 name = ""
 files = []
 directories = []
 parentDir = None

 def size(self):
  totalsize = 0
  for file in self.files:
   totalsize = totalsize + file.size
  for dir in self.directories:
   totalsize = totalsize + dir.size()
  return totalsize

class File:
 name = ""
 size = 0
root = Dir()
currentDirectory = root


allDirectories = [root]

currentDirectory = root
while True:
 line = input()
 if line:
  match line.split():
   case ["$", command]: pass
   case ["dir", dirname]: pass
   case ["$", "cd", dir]:
    if dir == "/":
     currentDirectory = root
    elif dir == "..":
     currentDirectory = currentDirectory.parentDir
    else:
     newdirectory = None
     for directory in currentDirectory.directories:
      if directory.name == dir:
       newdirectory = directory
     if newdirectory:
      currentDirectory = newdirectory
     else:
      newdirectory = Dir()
      newdirectory.name = dir
      newdirectory.directories = []
      newdirectory.files = []
      newdirectory.parentDir = currentDirectory
      currentDirectory.directories.append(newdirectory)
      currentDirectory = newdirectory
      allDirectories.append(newdirectory)
   case [size, filename]:
    file = File()
    file.name = filename
    file.size = int(size)
    currentDirectory.files.append(file)
 else:
  break

def solve_puzzle1():
 totalsize = 0
 for dir in allDirectories:
  if dir.size() <= 100000:
   totalsize += dir.size()

 print(f'The max count is {totalsize}')


def solve_puzzle2():
 unusedSpace = 70000000-root.size()
 requiredSpace = 30000000 - unusedSpace
 dirSize = 70000000
 for dir in allDirectories:
  if dir.size() >= requiredSpace:
   if dirSize > dir.size():
    dirSize = dir.size()

 print(f'The max count is {dirSize}')


solve_puzzle2()



