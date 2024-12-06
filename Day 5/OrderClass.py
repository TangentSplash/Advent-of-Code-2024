class OrderClass:
    def __init__(self,number,before):
        self.number = number
        self.numsBefore = [before]
        self.latestIndex = -1
    
    def checkShouldBeBefore(self,listOfAfter):
        for after in listOfAfter:
            if (after in self.numsBefore):
                self.latestIndex = listOfAfter.index(after)
                return False
        return True
    
    def append(self, num):
        self.numsBefore.append(num)
        
    def reorderSubList(self,list,i):
        num = list.pop(i+1+self.latestIndex)
        list.insert(i,num)
        return list