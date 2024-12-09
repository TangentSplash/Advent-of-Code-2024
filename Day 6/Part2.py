from GuardClass import Guard
INPUT ='Day 6/input.txt'
Fileinput = open(INPUT,"r")
locmap = Fileinput.readlines()

# NOTES:
# Only worth placing obstruction on guard's current route

# How to identify loop?:
# Same direction on same position ever

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

path = set()
loops = 0        

xStart,yStart = findGuardStart()
guard = Guard(xStart,yStart,locmap.copy())
while(guard.getNormalPath() != 0):
    path.add((guard.getX(),guard.getY()))
    
for pos in path:
    guard = Guard(xStart,yStart,locmap.copy())
    loops += guard.tryNewObsticale(pos)

print('The number of loops was ' + str(loops))