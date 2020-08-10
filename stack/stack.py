from collections import deque

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
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, value):
        self.next_node = value


class LinkedList:
    # Holds on to the first node and the last node
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, new_node):
        node = Node(new_node)

        if self.head is None and self.tail is None:
            self.tail = node
            self.head = node
        else:
            previous = self.tail
            previous.set_next_node(node)
            self.tail = node

    def remove_from_tail(self):
        if self.head and self.tail is None:
            return None

        elif self.head == self.tail:
            deleted = self.head.get_value()
            self.head = None
            self.tail = None
            return deleted

        else:
            deleted = self.tail.get_value()
            # The only way to get the second to last value is to go through the whole list from the beginning
            current = self.head
            # Keep iterating until the next_node == the deleted node
            while current.get_next_node() != self.tail:
                current = current.get_next_node()

            self.tail = current
            self.tail.set_next_node(None)
            return deleted

    def remove_head(self):
        deleted = self.head.get_value()
        if self.head and self.tail is None:
            return None

        elif self.head == self.tail:
            deleted = self.head.get_value()
            self.head = None
            self.tail = None
            return deleted

        else:
            self.head = self.head.get_next_node()
            return deleted

    def contains(self):
        count = 1
        current = self.head

        while current is not None:
            count += 1
            current = current.get_next_node()


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.storage.contains()

    def push(self, value):
        self.storage.add_to_tail(Node(value))

    def isEmpty(self):
        return self.storage.head == None and self.storage.tail == None

    def length(self):
        if(self.isEmpty()):
            return 0

        else:
            return self.storage.contains

    def pop(self):
        if(self.isEmpty()):
            return None
        else:
            return self.storage.pop()
