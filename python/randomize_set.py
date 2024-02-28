import random
class RandomizedSet:
    def __init__(self) -> None:
        self.indexes_dict = dict()
        self.randomized_set = list()

    def insert(self, val):
        if self.indexes_dict.get(val):
            return False
        else:
            self.randomized_set.append(val)
            self.indexes_dict[val] = len(self.randomized_set)
            return True

    def remove(self, val):
        if not self.indexes_dict.get(val):
            return False
        else:
            self.indexes_dict.pop(val)
            self.randomized_set.remove(val)
            return True

    def getRandom(self):
        if len(self.randomized_set) != 0:
            index = random.randrange(0,len(self.randomized_set))
            return self.randomized_set[index]
        
print(random.randrange(0,4))