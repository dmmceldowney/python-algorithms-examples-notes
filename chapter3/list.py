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
        self.size = 0


    def isEmpty(self):
        return self.head == None

    
    # this adds a node to the BEGINNING of the list
    def add(self, item):
        temp = Node(item)
        old_head = self.head
        temp.setNext(old_head)
        self.head = temp
        self.size += 1


    def size(self):
        return self.size
    

    def search(self, item):
        current_node = self.head
        while current is not None:
            if current_node.getData() == item:
                return True
            else:
                current_node = current_node.getNext()
        return False


    def remove(self, item):
        # Set base variables
        current_node = self.head
        previous_node = None
        found = False

        # traverse through the list
        while not found:
            # if the node's data == the item, break the loop
            if current_node.getData() == item:
                found = True
            else:
                previous_node = current_node
                current_node = current_node.getNext()
        
        # if the previous node is empty and we found the data
        if previous_node == None and found:
            # set the head of the list to the next node; we're just removing the node from the list
            self.head = current_node.getNext()
        # otherwise, if the data is found and there is a previous node, we use THAT data
        elif found:
            previous_node.setNext(current.getNext())

        self.size -= 1


    def append(self, item):
        current_node = self.head
        new_node = Node(item)

        if current_node is None:
            self.head = new_node
        else:
            while current_node is not None:
                if current_node.getNext() is None:
                    current_node.setNext(new_node)
        
        self.size += 1


    def insert(self, item, position):
        current_node = self.head
        previous_node = None
        new_node = Node(item)
        count = 0

        
        if position == 0:
            self.add(new_node)
        else:
            # Keep getting nodes until we're in position
            while count != position:
                previous_node = current_node
                current_node = current_node.getNext()
                count += 1

            new_node.setNext(current_node)
            previous_node.setNext(new_node)

        self.size += 1
            
    
    def index(self, item):
        current_node = self.head
        count = 0

        while current_node is not None:
            if current_node.getData() == item:
                return count
            else:
                current_node = current_node.getNext()
                count += 1


    def pop(self, position = None): # O(log n)
        if position is None:
            position =  self.size
        current_node = self.head
        previous_node = None
        next_node = current_node.getNext()
        count = 0
        # Check to see if we're at position

        while position != count: # O(log n)
            previous_node = current_node
            current_node = next_node
            next_node = current_node.getNext()
            count += 1

        data = current_node.getData()
        previous_node.setNext(next_node)

        self.size -= 1 
        
        return data


        



        """

        if next_node is None:
            self.head = None
        else:
            while next_node is not None:
                previous_node = current_node
                current_node = current_node.getNext()
                next_node = current_node.getNext()
            
            previous_node.setNext(None)
        
        return current_node.getData()
        """            

            
            
        



