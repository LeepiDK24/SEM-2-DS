from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)  
            return self.cache[key]
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)  
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  


lru_cache = LRUCache(2)
lru_cache.put(1, 1)           
lru_cache.put(2, 2)           
print(lru_cache.get(1))      
lru_cache.put(3, 3)           
print(lru_cache.get(2))      
lru_cache.put(4, 4)           
print(lru_cache.get(1))       
print(lru_cache.get(3))       
print(lru_cache.get(4))       