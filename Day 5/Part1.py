import OrderClass
from math import floor

INPUT ='Day 5/input.txt'
Fileinput = open(INPUT,"r")
Input = Fileinput.readlines()

rules = {}
def createOrder(line):
    order = line.split('|')
    first = int(order[0])
    second = int(order[1])
    if (second in rules):
        orderRule = rules.get(second)
        orderRule.append(first)
    else:
        newOrderRule = OrderClass.OrderClass(second,first)
        rules[second] = newOrderRule
        
sum = 0

getOrder = True
for line in Input:
    if (line.isspace()):
        getOrder = False
    elif (getOrder):
        createOrder(line)
    else:
        valid = True
        sequenceString = line.split(',')
        sequence = [int(item) for item in sequenceString]
        for number in sequence:
            if number in rules:
                rule = rules[number]
                i = sequence.index(number)
                if(not rule.checkShouldBeBefore(sequence[i+1:])):
                    valid = False
                    break
        if(valid):
            sum += sequence[floor(len(sequence) / 2)]
                    
print("The sum is " + str(sum))