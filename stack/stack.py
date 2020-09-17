"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
# Stack class using array as the underlying storage structure.
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        pass
        return self.size

    def push(self, value):
        self.storage.append(value)
        self.size = self.size + 1
        pass

    def pop(self):
        pass
        if self.size > 0:
            index_to_pop = self.size - 1 
            self.size = self.size - 1
            return self.storage.pop(index_to_pop)
            pass

# Stack class using linked list.
class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, new_next):
        self.next_node = new_next        

class Stack:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def __len__(self):
        return self.size

    def push(self, value):
        new_node = Node(value)
        self.size += 1
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_next_node(self.head)
            self.head = new_node
        pass

    def pop(self):
        if self.head is None:
            return None  
        else:
            ret_value = self.head.get_value()
            self.head = self.head.get_next_node()
            self.size -= 1    
            return ret_value

# With arrays you have access to index and length method. Linked lists on the other hand keep track of head and tail elements.