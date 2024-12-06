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
        wasOrdered = True
        sequenceString = line.split(',')
        sequence = [int(item) for item in sequenceString]
        sequence_copy = sequence.copy()
        for number in sequence_copy:
            if number in rules:
                rule = rules[number]
                valid = False
                while (not valid):
                    i = sequence.index(number)
                    valid = True
                    if(not rule.checkShouldBeBefore(sequence[i+1:])):
                        wasOrdered = False
                        valid = False
                        rule.reorderSubList(sequence,i)
        if(not wasOrdered):
            sum += sequence[floor(len(sequence) / 2)]
                    
print("The sum is " + str(sum))