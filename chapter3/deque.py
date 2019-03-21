# A deque is a ADT that allows insertions and removals from the beginning and the end of the structure
class Deque():

    def __init__(self):
        self.items = []


    def addFront(self, item):
        self.items.insert(0, item) # O(n)


    def addRear(self, item):
        self.items.append(item) # O(1)


    def removeFront(self):
        return self.items.pop(0) # O(n)


    def removeRear(self):
        return self.items.pop() # O(1)


    def isEmpty(self):
        return self.items == []

    
    def size(self):
        return len(self.items)