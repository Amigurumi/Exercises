# A stack representation with just a few basic operations
class Stack:
    def __init__(self):
        self.storage = []
    
    def push(self, element):
        self.storage.append(element)
    
    def pop(self):
        return self.storage.pop()

    def is_empty(self):
        return len(self.storage) == 0
    
    # Empty this stack
    def clear(self):
        self.storage = []

    # Return a new Stack whose elements are reversed from what's in this Stack
    def reverse(self):
        reversed = Stack()
        
    


# Testing
stack = Stack()
stack.push('one')
stack.push('two')
stack.push('three')
stack.push('four')

reversed = stack.reverse()
while not reversed.is_empty():
    element = reversed.pop()
    print(element)