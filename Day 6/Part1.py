from GuardClass import Guard
INPUT ='Day 6/input.txt'
Fileinput = open(INPUT,"r")
locmap = Fileinput.readlines()

GUARD = '^'
WALL = '#'
UNVISITED = '.'
VISITED = 'X'

for i in range(len(locmap)): 
    line = locmap[i]
    line = list(map(str,line))
    line.remove('\n')
    locmap[i] = line

def findGuardStart():
    for line in locmap: #string to list conversion for each line
        try: 
            i = line.index(GUARD)
            j = locmap.index(line)
            return i,j
        except:
            pass
        
x,y = findGuardStart()
guard = Guard(x,y,locmap)
locations = guard.start()
print('The number of locations visited is ' + str(locations))