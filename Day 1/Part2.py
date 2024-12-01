INPUT='Day 1/input.txt'
Fileinput= open(INPUT,"r")
Input=Fileinput.readlines()

listA = []
listB = []
for line in Input:
    numbers = line.split('   ')
    listA.append(int(numbers[0]))
    listB.append(int(numbers[1]))
listA.sort()
listB.sort()

lastA = 0 
multiplier = 0
similarity = 0
for a in listA:
    if (a != lastA):
        multiplier=listB.count(a) 
    similarity += (a * multiplier)
    
print('The similarity score is '+str(similarity))