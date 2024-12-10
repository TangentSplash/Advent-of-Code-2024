INPUT ='Day 7/input.txt'
Fileinput = open(INPUT,"r")
Input = Fileinput.readlines()

ADD = 0
MULT = 1
    
def tryOperation(target, sum,operands, operation):
    thisOperand = operands.pop(0)
    match operation:
        case 0: # Add
            sum = sum + thisOperand
        case 1: # Mult
            sum = sum * thisOperand
        case _:
            print('Error, invalid operation')
    if (sum > target):
        return False
    elif (len(operands) == 0):
        if (sum == target):
            return True
        else:
            return False
    else:
        return tryOperations(target, sum, operands)
    
def tryOperations(target, sum, operands):
    if (tryOperation(target, sum, operands.copy(), ADD)):
            return True
    else:
        return tryOperation(target, sum, operands.copy(), MULT)
    
totalCalibration = 0
for line in Input:
    vals = line.split(': ')
    target = int(vals[0])
    operands = [int(i) for i in vals[1].split(' ')]
    if(tryOperations(target,operands[0],operands[1:])):
        totalCalibration += target

print('The total calibration is ' + str(totalCalibration))
