from random import choice

class RandomizedSet:
    def __init__(self):
        self.randset = set()

    def insert(self, val: int) -> bool:
        isAlreadyInSet = val in self.randset
        if not isAlreadyInSet: self.randset.add(val)
        return not isAlreadyInSet

    def remove(self, val: int) -> bool:
        isAlreadyInSet = val in self.randset
        if isAlreadyInSet: self.randset.remove(val)
        return isAlreadyInSet

    def getRandom(self) -> int:
        return choice(tuple(self.randset))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()