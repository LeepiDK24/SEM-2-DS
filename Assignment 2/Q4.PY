import random

class RandomizedCollection:
    def __init__(self):
        self.values = []
        self.indices = {}

    def insert(self, val: int) -> bool:
        self.values.append(val)
        if val not in self.indices:
            self.indices[val] = set()
        self.indices[val].add(len(self.values) - 1)
        return len(self.indices[val]) == 1

    def remove(self, val: int) -> bool:
        if val not in self.indices or not self.indices[val]:
            return False
        remove_idx = self.indices[val].pop()
        last_val = self.values[-1]
        self.values[remove_idx] = last_val
        if self.indices[last_val]:
            self.indices[last_val].add(remove_idx)
            self.indices[last_val].discard(len(self.values) - 1)
        self.values.pop()
        if not self.indices[val]:
            del self.indices[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)
