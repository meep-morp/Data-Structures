"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

Search rules:
    1. The left side is the smaller value
    2. The right side is the larger value
    3. Duplicates go to the right of its twin

Runtime Type ->
Logarithmic: O(log^2 n)

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

from tkinter import *
import random
from queue import Queue
# STRETCH
# Using Tkinter to display the binary tree structure
master = Tk()
canvas_width = 900
canvas_height = 900
w = Canvas(master, width=canvas_width, height=canvas_height)

l_r_x = 110
l_r_y = 85
l_x = 90
l_y = 70


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

        self.x = canvas_width / 2
        self.y = 25

    # Insert the given value into the tree
    def insert(self, value):
        # check if the value is less than the current node's value
        if value < self.value:
            # LEFT
            # does the current node have a left child?
            if self.left and self.right:
                self.left.x = self.x - l_r_x
                self.left.y = self.y + l_r_y

            if self.left:
                self.left.insert(value)
            # otherwise, it doesn't have a left child
            # we can park the new node here
            else:
                self.left = BSTNode(value)
                self.left.x = self.x - l_x
                self.left.y = self.y + l_y
        # otherwise the value is greater or equal to the current node's value
        #  RIGHT
        else:
            if self.left and self.right:
                self.right.x = self.x + l_r_x
                self.right.y = self.y + l_r_y
            # does the current node have a right child?
            if self.right:
                # if it does, call the right child's `insert` method to repeat the process
                self.right.insert(value)
            # otherwise, it doesn't have a right child
            # we can park the new node here
            else:
                self.right = BSTNode(value)
                self.right.x = self.x + l_x
                self.right.y = self.y + l_y

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        elif target <= self.value:
            if self.left != None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right == None:
                return False
            else:
                return self.right.contains(target)


# Return the maximum value found in the tree


    def get_max(self):
        max = self
        while max.right != None:
            print("max")
            max = max.right
        return max.value

    # Call the function `fn` on the value of each node
    # Depth First Traversal
    def for_each(self, fn):
        fn(self.value)
        if self.right:
            self.right.for_each(fn)
        if self.left:
            self.left.for_each(fn)

    def display(self):
        w.create_text(self.x, self.y, fill="black",
                      font="Times 20 italic bold", text=self.value)
        w.create_oval(self.x + 20, self.y + 20, self.x - 20, self.y - 20)
        if self.right:
            w.create_line(self.x, self.y, self.right.x,
                          self.y + 55, fill="black")
            self.right.display()
        if self.left:
            w.create_line(self.x, self.y, self.left.x,
                          self.y + 55, fill="black")
            self.left.display()

    # Part 2 === === === === ===

    # Print all the values in order from low to high
    # Hint: Use a recursive, depth first traversal
    def in_order_print(self):
        if self == None:
            pass
        if self.left:
            self.left.in_order_print()
        print(self.value)

        if self.right:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        s = Queue()
        s.enqueue(self)

        if self.left:
            self.left.bft_print()
        if self.right:
            self.right.bft_print()
        print(s.dequeue().value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_print(self):
        pass

    # Print Post-order recursive DFT
    def post_order_print(self):
        pass


"""
This code is necessary for testing the `print` methods
"""

# For Visuals
# for i in range(12):
#     bst.insert(random.randint(1, 99))
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_print()
print("in order")
bst.in_order_print()
print("post order")
bst.post_order_print()

bst.display()
w.pack()
mainloop()
