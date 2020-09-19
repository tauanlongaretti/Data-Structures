"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
#Queue class using array as the underlying storage structure.
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.append(value)
        self.size += 1

    def dequeue(self):
        if self.size is 0:
            return None
        else:
            ret_value = self.storage[0]
            self.storage.pop(0)
            self.size -= 1
            return ret_value

#Queue class using linked list.
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
        
class Queue:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node    
        else:
            new_node.set_next_node(self.head)
            self.head = new_node
        self.size += 1

    def dequeue(self):
        if self.head is None:
            return None
        ret_value = self.tail.get_value()    
        if self.head == self.tail:           
            self.head = None
            self.tail = None
        else:
            cur_node = self.head
            while cur_node.get_next_node() is not self.tail:
                cur_node = cur_node.get_next_node()
            cur_node.set_next_node(None)
            self.tail = cur_node
        self.size -= 1
        return ret_value
        

# the difference between using an array vs. a linked list when implementing a queue is that for linked lists you would have to loop between the entire list as you can't target the index. 