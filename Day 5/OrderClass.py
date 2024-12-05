class OrderClass:
    def __init__(self,number,before):
        self.number = number
        self.numsBefore = [before]
    
    def checkShouldBeBefore(self,listOfAfter):
        for after in listOfAfter:
            if (after in self.numsBefore):
                return False
        return True
    
    def append(self, num):
        self.numsBefore.append(num)