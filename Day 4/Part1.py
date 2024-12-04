INPUT ='Day 4/input.txt'
Fileinput = open(INPUT,"r")
letters = Fileinput.readlines()

WORD = "XMAS"

length = len(letters[0])
height = len(letters)

def findNextLetter(X,Y,i,j,num):
    x = X + (i * num)
    y = Y + (j * num)
    if (letters[y][x] == WORD[num]):
        if (num < len(WORD) - 1):
            return findNextLetter(X,Y,i,j,num + 1)
        else:
            return True # Found the last letter in a row
    return False
    
numberWordFound = 0
    
for Y in range(0,height):
    for X in range(0,length):
        if (letters[Y][X] == WORD[0]):
            for j in range(-1,2):
                endLocation = Y + (j * (len(WORD) - 1))
                if (endLocation < 0 or endLocation >= height):
                    continue
                for i in range (-1,2):
                    endLocation = X + (i * (len(WORD) - 1))
                    if (endLocation < 0 or endLocation >= length):
                        continue
                    if(findNextLetter(X,Y,i,j,1)):
                        numberWordFound += 1
            
print(WORD + " was found " + str(numberWordFound) + " times")