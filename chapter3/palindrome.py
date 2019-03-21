from deque import Deque

def palindromeCheck(word):
    deque = Deque()

    for letter in word:
        deque.addFront(letter)

    while deque.size() > 1:
        front_letter = deque.removeFront()
        back_letter = deque.removeRear()

        if front_letter != back_letter:
            return False

    return True

print(palindromeCheck('satanoscillatemymetallicsonatas'))