INPUT ='Day 9/input.txt'
Fileinput = open(INPUT,"r")
diskmap = Fileinput.readline()

EMPTY = -1
id = 0
memory = []
i = 0

def addMemory(num, id):
    memory.extend([id] * num)
    
for digit in diskmap:
    if (digit != '\n'):
        digit = int(digit)
        if (i == 0):
            addMemory(digit,id)
            id += 1
        else:
            addMemory(digit, EMPTY)
        i = (i+1)%2
    
i = 0
while (i < len(memory)):
    if(memory[i] == EMPTY):
        memory[i] = memory.pop(-1)
        while(memory[-1] == EMPTY):
            memory.pop(-1)
    i += 1
    
checksum = 0    
for i in range(0,len(memory)):
    checksum += (i * memory[i])
    
print('The checksum is ' +str(checksum))