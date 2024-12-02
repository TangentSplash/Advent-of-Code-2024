INPUT ='Day 2/input.txt'
Fileinput = open(INPUT,"r")
Input = Fileinput.readlines()

def checkReport(report):
    increasing = 2 # Not increasing or decreasing yet
    first = int(report.pop(0))
    for strNext in report:
        next = int(strNext)
        dist = abs(first-next)
        if (not(((first < next and increasing != 0) or (first > next and increasing != 1)) and dist >= 1 and dist <= 3)):
            return 0
        else:
            if (increasing == 2):
                if (first < next):
                    increasing = 1
                else:
                    increasing = 0
            first = next
    return 1

numSafe = 0
for line in Input:
    nums = list(map(int,line.split(' '))) # Cast to int list
    
    safe = checkReport(nums[:])
    i=0
    while(not safe and i<len(nums)):
        numsDampened = nums[:i]+nums[i+1:]
        i += 1
        safe = checkReport(numsDampened)
    if (safe):
        numSafe += 1
        
    
print("\nThe number of safe reports are " +str(numSafe)+ "\n")