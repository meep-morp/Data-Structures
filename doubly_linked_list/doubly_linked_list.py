"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next


"""
Our doubly-linked list class. It holds references to
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node != None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
        new_node = ListNode(value)
        if self.length:
            new_node.next = self.head
            self.head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node
        self.length += 1

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        if self.length == 1:
            value = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        else:
            value = self.head.value
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
            return value

    """
    Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        new_node = ListNode(value)
        if self.length:
            new_node.prev = self.tail
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node
        self.length += 1

    """
    Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        if self.length == 1:
            value = self.tail.value
            self.tail = None
            self.head = None
            self.length -= 1
            return value
        else:
            value = self.tail.value
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
            return value

    """
    Removes the input node from its current spot in the
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        if self.length > 1:
            if node != self.tail:
                node.prev.next = node.next
                node.next.prev = node.prev
            else:
                node.prev.next = None
                self.tail = node.prev
            self.head.prev = node
            node.next = self.head
            node.prev = None
            self.head = node

    """
    Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        if self.length > 1:
            if node != self.head:
                node.prev.next = node.next
                node.next.prev = node.prev
            else:
                node.next.prev = None
                self.head = node.next
            self.tail.next = node
            node.prev = self.tail
            node.next = None
            self.tail = node

    """
    Deletes the input node from the List, preserving the
    order of the other elements of the List.
    """

    def delete(self, node):
        if self.length > 1:
            if node == self.head:
                node.next.prev = None
                self.head = node.next
            elif node == self.tail:
                node.prev.next = None
                self.tail = node.prev
            else:
                node.prev.next = node.next
                node.next.prev = node.prev
            self.length -= 1
        elif node == self.head:
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            return "Hey that node isn't in this list!"

    """
    Finds and returns the maximum value of all the nodes
    in the List.
    """

    def get_max(self):
        if self.length:
            max = self.head.value
            current = self.head
            while current != None:
                if current.value > max:
                    max = current.value
                current = current.next
            return max

# Interview Question
# Print out all of the numbers in the following array that are divisible by 3:


def div_by_3(list):
    for num in list:
        if(num % 3 == 0):
            print(num)
        else:
            pass


list = [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]
div_by_3(list)
# The expected output for the above input is :
# 27
# 81
# 9
# 27
# 99
# 63
# 42
