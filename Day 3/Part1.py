from re import findall as findall
INPUT ='Day 3/input.txt'
Fileinput = open(INPUT,"r")
Input = Fileinput.read()

multiplies = findall(r'mul\(\d+,\d+\)',Input)

sum = 0
for multiply in multiplies:
    operands = findall(r'\d+',multiply)
    mult = int(operands[0]) * int(operands[1])
    sum += mult
    
print('The sum is ' + str(sum))