from math import sin,cos,pi
import copy

GUARD = '^'
WALL = '#'
UNVISITED = '.'
VISITED = 'X'
PLACED = 'O'

class Guard:
    def __init__(self,x,y,map):
        self.x = x
        self.y = y
        self.i = 0
        self.j = -1
        self.map = copy.deepcopy(map)
        self.map[y][x] = VISITED
        self.xbound = len(map[0])
        self.ybound = len(map)
        self.visitedPositions = 1
        self.heading = (3*pi/2)
        self.past_locations = {}
        self.loops = 0
        
    def move(self):
        X = self.x + self.i
        Y = self.y + self.j
        
        if (X < 0 or X >= self.xbound or Y < 0 or Y >= self.ybound):
            return 0
        
        else:
            match self.map[Y][X]:
                case value if value == WALL or value == PLACED:
                    self.turnRight()
                    return self.move()
                case value if value == UNVISITED:
                    self.map[Y][X] = VISITED
                    self.visitedPositions += 1
            if (self.map[Y][X] == VISITED):
                self.x = X
                self.y = Y
                locationKey = str(X)+","+str(Y)
                if (locationKey in self.past_locations and self.heading in self.past_locations[locationKey]):
                    return 2
                if (locationKey in self.past_locations):
                    self.past_locations[locationKey].append(self.heading)
                else:
                    self.past_locations[locationKey] = [self.heading]
            return 1
        
    def turnRight(self):
        self.heading = (self.heading - pi/2) % (2*pi)
        self.i = -int(cos(self.heading))
        self.j = int(sin(self.heading))
        
        
    def start(self):
        while(self.move()):
            pass
        return self.visitedPositions
    
    def getLoops(self):
        return self.loops
    
    def tryNewObsticale(self,position):
        obsX = position[0]
        obsY = position[1]
        self.map[obsY][obsX] = PLACED
        status = 1
        while (status == 1):
            status = self.move()
        if (status == 2):
            return 1
        return 0
    
    def getNormalPath(self):
        return self.move()
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
         
                    