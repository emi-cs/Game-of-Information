import random
import defs

class Info():
    def __init__(self, id):
        self.id = id
        self.capacity = 0
        # self.popularity = 0 #how many % of population do you think will find this piece of information useful
        self.count = 1
        self.firstTime = True

    def randomizeCapacity(self):
        self.capacity = random.randint(1, defs.numOfAgent // 2)

    def increaseCount(self):
        self.count += 1

    def capacityPassed(self) -> bool: 
        if self.count <= self.capacity:
            return False
        else:
            return True
        
    def getSaturation(self) -> float:
        return self.count/self.capacity

