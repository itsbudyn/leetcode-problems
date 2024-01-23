from random import choice

class RandomizedCollection:
    def __init__(self):
        self.randcol = list()

    def insert(self, val: int) -> bool:
        isAlreadyInCol = val in self.randcol
        self.randcol.append(val)
        return not isAlreadyInCol

    def remove(self, val: int) -> bool:
        isAlreadyInCol = val in self.randcol
        if isAlreadyInCol: self.randcol.remove(val)
        return isAlreadyInCol

    def getRandom(self) -> int:
        return choice(self.randcol)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()