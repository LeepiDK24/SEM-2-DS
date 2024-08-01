class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(index - 1):
            if current is None:
                raise IndexError("Index out of range")
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def delete(self, index):
        if self.head is None:
            raise IndexError("Index out of range")
        if index == 0:
            self.head = self.head.next
            return
        current = self.head
        for _ in range(index - 1):
            if current is None or current.next is None:
                raise IndexError("Index out of range")
            current = current.next
        current.next = current.next.next

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def is_empty(self):
        return self.head is None

    def rotate(self, k):
        if not self.head or k == 0:
            return
        size = self.size()
        k %= size
        if k == 0:
            return
        current = self.head
        for _ in range(size - k - 1):
            current = current.next
        new_head = current.next
        current.next = None
        tail = new_head
        while tail.next:
            tail = tail.next
        tail.next = self.head
        self.head = new_head

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def merge(self, other):
        if not self.head:
            self.head = other.head
            return
        if not other.head:
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = other.head

    def interleave(self, other):
        dummy = Node()
        tail = dummy
        p1, p2 = self.head, other.head
        while p1 and p2:
            tail.next = p1
            p1 = p1.next
            tail = tail.next
            tail.next = p2
            p2 = p2.next
            tail = tail.next
        tail.next = p1 if p1 else p2
        self.head = dummy.next

    def middle(self):
        slow, fast = self.head, self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.value if slow else None

    def index_of(self, value):
        current = self.head
        index = 0
        while current:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1

    def split(self, index):
        if index == 0:
            new_list = SinglyLinkedList()
            new_list.head = self.head
            self.head = None
            return new_list
        current = self.head
        for _ in range(index - 1):
            if current is None:
                raise IndexError("Index out of range")
            current = current.next
        new_list = SinglyLinkedList()
        new_list.head = current.next
        current.next = None
        return new_list


sll = SinglyLinkedList()
sll.append(1)
sll.append(2)
sll.append(3)
print("Size:", sll.size())  
print("Middle:", sll.middle())  
sll.rotate(1)
print("After rotation:")
current = sll.head
while current:
    print(current.value, end=" ")  
    current = current.next
print()
sll.reverse()
print("After reversal:")
current = sll.head
while current:
    print(current.value, end=" ") 
    current = current.next
print()
