class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashMapSeparateChaining:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.buckets = [None] * self.capacity

    def hash(self, key):
        return hash(key) % self.capacity

    def find(self, key):
        index = self.hash(key)
        current = self.buckets[index]
        while current:
            if current.key == key:
                return True
            current = current.next
        return False

    def insert(self, key, value):
        index = self.hash(key)
        new_node = Node(key, value)
        if not self.buckets[index]:
            self.buckets[index] = new_node
        else:
            current = self.buckets[index]
            while current:
                if current.key == key:
                    current.value = value
                    return
                if not current.next:
                    break
                current = current.next
            current.next = new_node

    def remove(self, key):
        index = self.hash(key)
        current = self.buckets[index]
        prev = None
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.buckets[index] = current.next
                return
            prev = current
            current = current.next


hashmap = HashMapSeparateChaining()
hashmap.insert("key1", "value1")
hashmap.insert("key2", "value2")
print(hashmap.find("key1"))  
print(hashmap.find("key3"))  
hashmap.remove("key1")
print(hashmap.find("key1"))  
