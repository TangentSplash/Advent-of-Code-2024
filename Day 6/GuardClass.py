from math import sin,cos,pi
GUARD = '^'
WALL = '#'
UNVISITED = '.'
VISITED = 'X'

class Guard:
    def __init__(self,x,y,map):
        self.x = x
        self.y = y
        self.i = 0
        self.j = -1
        self.map = map
        self.map[y][x] = VISITED
        self.xbound = len(map[0])
        self.ybound = len(map)
        self.visitedPositions = 1
        self.heading = (3*pi/2)
        
    def move(self):
        X = self.x + self.i
        Y = self.y + self.j
        
        if (X < 0 or X >= self.xbound or Y < 0 or Y >= self.ybound):
            return False
        
        else:
            match self.map[Y][X]:
                case value if value == WALL:
                    self.turnRight()
                case value if value == UNVISITED:
                    self.map[Y][X] = VISITED
                    self.visitedPositions += 1
            if (self.map[Y][X] == VISITED):
                self.x = X
                self.y = Y
            return True
        
    def turnRight(self):
        self.heading = (self.heading - pi/2) % (2*pi)
        self.i = -int(cos(self.heading))
        self.j = int(sin(self.heading))
        
        
    def start(self):
        while(self.move()):
            pass
        return self.visitedPositions
                    