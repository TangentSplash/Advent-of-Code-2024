INPUT ='Day 2/input.txt'
Fileinput = open(INPUT,"r")
Input = Fileinput.readlines()

numSafe = 0
for line in Input:
    nums = line.split(' ')
    safe = True
    increasing = 2 # Not increasing or decreasing yet
    first = int(nums.pop(0))
    for strNext in nums:
        next = int(strNext)
        dist = abs(first-next)
        if (not((increasing == 2 or (first < next and increasing != 0) or (first > next and increasing != 1)) and dist >= 1 and dist <= 3)):
            safe = False
            break
        else:
            if (increasing == 2):
                if (first < next):
                    increasing = 1
                else:
                    increasing = 0
            first = next
    if (safe):
        numSafe += 1
        
print("\nThe number of safe reports are " +str(numSafe)+ "\n")