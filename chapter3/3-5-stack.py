# Implementing a Stack in Python
class Stack:
    def __init__(self):
        self.items = []

    
    def isEmpty(self):
        return self.items == []

    
    def push(self, item):
        self.items.append(item)

    
    def pop(self):
        return self.items.pop()


    def peek(self):
        return self.items[len(self.items)-1]


    def size(self):
        return len(self.items)


# Testing knowledge:
# Write a function revstring(mystr) that uses a stack to reverse the characters in a string.

def revstring(mystr):
    stack = Stack()
    for c in mystr:
        stack.push(c)

    new_str = ""

    while stack.size() > 0:
        new_str += stack.pop()
        
    return new_str


s = 'This is a test string'
print(s)
print(revstring(s))