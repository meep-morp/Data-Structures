from singly_linked_list import LinkedList, Node
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

   An array is a lot simpler to implement but can be slow since you keep track of all the items
"""


# With lists
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         self.storage.append(value)

#     def length(self):
#         return len(self.storage)

#     def isEmpty(self):
#         return len(self.storage) == 0

#     def pop(self):
#         if(self.isEmpty()):
#             return None
#         else:
#             return self.storage.pop()


# With Linked Lists

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.storage.length()

    def push(self, value):
        self.storage.add_to_tail(Node(value))

    def isEmpty(self):
        return self.storage.head == None and self.storage.tail == None

    def length(self):
        if(self.isEmpty()):
            return 0

        else:
            return self.storage.length()

    def pop(self):
        if(self.isEmpty()):
            return None
        else:
            node = self.storage.remove_from_tail()
            return node.get_value()
