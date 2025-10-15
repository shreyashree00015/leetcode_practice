class RandomizedSet:

    def __init__(self):
        self.list1 = []

    def insert(self, val: int) -> bool:
        if val in self.list1:
            return False
        else:
            self.list1.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.list1:
            self.list1.remove(val)
            return True
        else:
            return False
        
    def getRandom(self) -> int:
        import random
        return random.choice(self.list1)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()