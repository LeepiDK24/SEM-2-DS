class DynamicArray:
    def __init__(self, initial_capacity=4, resize_factor=2):
        self.size = 0
        self.capacity = initial_capacity
        self.resize_factor = resize_factor
        self.array = [None] * self.capacity

    def _resize(self, new_capacity):
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def insert(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        if self.size == self.capacity:
            self._resize(self.capacity * self.resize_factor)
        for i in range(self.size, index, -1):
            self.array[i] = self.array[i - 1]
        self.array[index] = value
        self.size += 1

    def delete(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]
        self.size -= 1
        self.array[self.size] = None

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def rotate(self, k):
        if self.size == 0:
            return
        k = k % self.size
        self.array = self.array[-k:] + self.array[:-k]

    def reverse(self):
        for i in range(self.size // 2):
            self.array[i], self.array[self.size - 1 - i] = self.array[self.size - 1 - i], self.array[i]

    def append(self, value):
        if self.size == self.capacity:
            self._resize(self.capacity * self.resize_factor)
        self.array[self.size] = value
        self.size += 1

    def prepend(self, value):
        self.insert(0, value)

    def merge(self, other):
        for i in range(other.size):
            self.append(other.array[i])

    def interleave(self, other):
        new_array = DynamicArray(initial_capacity=self.size + other.size)
        i, j = 0, 0
        while i < self.size or j < other.size:
            if i < self.size:
                new_array.append(self.array[i])
                i += 1
            if j < other.size:
                new_array.append(other.array[j])
                j += 1
        self.array = new_array.array
        self.size = new_array.size
        self.capacity = new_array.capacity

    def get_middle(self):
        if self.size == 0:
            return None
        return self.array[self.size // 2]

    def index_of(self, value):
        for i in range(self.size):
            if self.array[i] == value:
                return i
        return -1

    def split(self, index):
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        new_array = DynamicArray(initial_capacity=self.capacity)
        for i in range(index, self.size):
            new_array.append(self.array[i])
        self.size = index
        return new_array



da = DynamicArray()
da.append(1)
da.append(2)
da.append(3)
da.append(4)
print("Initial array:", [da.array[i] for i in range(da.size)]) 
da.insert(2, 5)
print("After insertion at index 2:", [da.array[i] for i in range(da.size)])  
da.delete(1)
print("After deletion at index 1:", [da.array[i] for i in range(da.size)])  
print("Size:", da.get_size())  
print("Is empty:", da.is_empty()) 
da.rotate(2)
print("After rotation by 2 positions:", [da.array[i] for i in range(da.size)])  
da.reverse()
print("After reversal:", [da.array[i] for i in range(da.size)])  
da.prepend(6)
print("After prepending 6:", [da.array[i] for i in range(da.size)]) 
middle_element = da.get_middle()
print("Middle element:", middle_element) 
index_of_4 = da.index_of(4)
print("Index of 4:", index_of_4)  
split_array = da.split(2)
print("After splitting at index 2:")
print("First part:", [da.array[i] for i in range(da.size)])  
print("Second part:", [split_array.array[i] for i in range(split_array.size)])  
