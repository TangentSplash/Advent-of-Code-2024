INPUT='Day 1/input.txt'
Fileinput= open(INPUT,"r")
Input=Fileinput.readlines()

sum = 0
listA = []
listB = []
for line in Input:
    numbers = line.split('   ')
    listA.append(int(numbers[0]))
    listB.append(int(numbers[1]))
listA.sort()
listB.sort()

for a in listA:
    b = listB.pop(0)  
    diff = abs(a-b)
    sum += diff
    
print('The sum is '+str(sum))