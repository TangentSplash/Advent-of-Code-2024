from re import findall as findall
INPUT ='Day 3/input.txt'
MULTIPLY = r'mul\(\d+,\d+\)' 
FULLREGEX = MULTIPLY + r"|do\(\)|don't\(\)"
print(MULTIPLY)

Fileinput = open(INPUT,"r")
Input = Fileinput.read()

def getMultiply(input):
    operands = findall(r'\d+',input)
    return int(operands[0]) * int(operands[1])

sum = 0
instructions = findall(FULLREGEX,Input)
ignore = False
for instruction in instructions:
    match instruction:
        case 'do()':
            ignore = False
        case "don't()":
            ignore = True
        case _:
            if (not ignore):
                sum += getMultiply(instruction)
            
    
print('The sum is ' + str(sum))