# Using a stack to get the recursive base converter to work instead of concatenation
# This should teach us something about Python's Stack Frames

from stack import Stack

rStack = Stack()

def toStr(n, base):
    convertString = "0123456789ABCDEF"
    while n > 0:
        if n < base:
            rStack.push(convertString[n])
        else:
            rStack.push(convertString[n % base])
        n = n // base
    res = ""
    while not rStack.isEmpty():
        # this is already a string because we used "convertString",
        # and that's why addition works here :)
        res = res + rStack.pop() 
    return res

