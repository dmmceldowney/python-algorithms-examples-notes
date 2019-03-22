# Create the Node class

class Node():
    
    def __init__(self, initial_data):
        self.data = initial_data
        self.next = None

    
    def setData(self, new_data):
        self.data = new_data


    def getData(self):
        return self.data

    
    def setNext(self, next_node): # adding a node to the linked list
        self.next = next_node


    def getNext(self):
        return self.next


class UnorderedList():
    
    def __init__(self):
        self.head = None


    def isEmpty(self):
        return self.head == None

    
    # this adds a node to the BEGINNING of the list
    def add(self, item):
        temp = Node(item)
        old_head = self.head
        temp.setNext(old_head)
        self.head = temp


    


