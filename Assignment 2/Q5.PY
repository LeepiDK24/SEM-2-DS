class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def get(self,index):
        if index < 0 or index >= self.size:
            return -1
        trav = self.head
        for i in range(index):
            trav = trav.next
        return trav.data

    def addAtHead(self,value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        self.size += 1

    def addAtTail(self,value):
        newNode = Node(value)
        if self.tail is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
        self.size += 1 

    def addAtIndex(self, index, value):
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(value)
        elif index == self.size:
            self.addAtTail(value)
        else:
            newNode = Node(value)
            trav = self.head
            for i in range(index):
                trav = trav.next
            newNode.prev = trav.prev
            newNode.next = trav
            trav.prev.next = newNode
            trav.prev = newNode
            self.size += 1
    
    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return
        trav = self.head
        for i in range(index):
            trav = trav.next
        if trav.prev is not None:
            trav.prev.next = trav.next
        if trav.next is not None:
            trav.next.prev = trav.prev
        if trav == self.head:
            self.head = trav.next
        if trav == self.tail:
            self.tail = trav.prev
        self.size -= 1
        del trav