import random

class RandomizedSet:

    def __init__(self):
        self.values = set()

    def insert(self, val: int) -> bool:
        ret = val not in self.values
        self.values.add(val)
        return ret

    def remove(self, val: int) -> bool:
        ret = val in self.values
        if ret:
            self.values.remove(val)
        return ret

    def getRandom(self) -> int:
        return random.choice(list(self.values))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()