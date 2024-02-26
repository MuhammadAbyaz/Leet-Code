class SmallestInfiniteSet:

    def __init__(self):
        self.smallest_infinite_set = set(i for i in range(1, 1000))

    def popSmallest(self) -> int:
        if len(self.smallest_infinite_set) != 0:
            temp = list(self.smallest_infinite_set)
            temp.sort()
            element = temp.pop(0)
            self.smallest_infinite_set.remove(element)
            return element
        else:
            return 0

    def addBack(self, num: int) -> None:
        if num in self.smallest_infinite_set:
            return
        else:
            self.smallest_infinite_set.add(num)
