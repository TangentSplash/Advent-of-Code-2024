INPUT ='Day 8/input.txt'
Fileinput = open(INPUT,"r")
locmap = Fileinput.readlines()

BLANK = '.'

for i in range(len(locmap)): 
    line = locmap[i]
    line = list(map(str,line))
    line.remove('\n')
    locmap[i] = line

height = len(locmap)
width = len(locmap[0])

antinodes = set()

def addValidAntinode(x, y, distX, distY, multpilier):
    antinodeX = x + (multpilier*distX)
    antinodeY = y + (multpilier*distY)
    while (antinodeX >= 0 and antinodeX < width and antinodeY >=0 and antinodeY < height):
        antinodes.add(str(antinodeX)+','+str(antinodeY))
        antinodeX = antinodeX + (multpilier*distX)
        antinodeY = antinodeY + (multpilier*distY)
        
for Y in range(0,height):
    for X in range(0,width):
        char = locmap[Y][X]
        if char != BLANK:
            antinodes.add(str(X)+','+str(Y))
            for j in range(Y,height):
                for i in range(0,width):
                    if (i != X and j!= Y and locmap[j][i] == char): 
                        # Found another of the same antenna
                        distX = i - X
                        distY = j - Y
                        # Antinode 1
                        addValidAntinode(i,j,distX,distY,1)
                        # Antinode 2
                        addValidAntinode(i,j,distX,distY,-1)
                        
numAntinodes = len(antinodes)
print("The number of antinodes is " + str(numAntinodes))