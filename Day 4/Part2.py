INPUT ='Day 4/input.txt'
Fileinput = open(INPUT,"r")
letters = Fileinput.readlines()

WORD = "MAS"

length = len(letters[0])
height = len(letters)

def findX_MAS(X,Y):
    if (X-1 >= 0 and X+1 < length and Y-1 >= 0 and Y+1 < height and letters[Y][X] == WORD[1]):  # Find the A
        for a in range(0,3):    # If can't find an M in the first 3 locations, this isn't an X-MAS
            i = (int(a < 2) * 2) - 1    # Odd way to get sequence [1,1,-1,-1]
            j = ((a % 2) * 2) - 1       # Similar way to get [-1,1,-1,1]
            x = X + i
            y = Y + j
            if (letters[y][x] == WORD[0] and letters[Y-j][X-i] == WORD[2] and ((letters[Y+j][X-i] == WORD[0] and letters[Y-j][X+i] == WORD[2]) or (letters[Y-j][X+i] == WORD[0] and letters[Y+j][X-i] == WORD[2]))):    # Find the M and corresponding S, then the M & S crossing that
                return True
    return False
    
numberWordFound = 0
    
for Y in range(0,height):
    for X in range(0,length):
        if (findX_MAS(X,Y)):
            numberWordFound += 1
            
print("X-" + WORD + " was found " + str(numberWordFound) + " times")