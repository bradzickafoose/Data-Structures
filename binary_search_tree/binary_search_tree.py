import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
      # check if new value is less than current node
      if value < self.value:
        # if there is no self.left value
        if not self.left:
          # set the new left child to be new value
          self.left = BinarySearchTree(value)
        else:
          self.left.insert(value)

      # the new value is greater than the current node
      # go right
      else:
        if not self.right:
          self.right = BinarySearchTree(value)
        else:
          self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if the root node, is the target value, we found the value
        if self.value == target:
          return True
        # if target is smaller, go left
        if target < self.value:
          if not self.left:
            return False
          else:
            return self.left.contains(target)

        # target is greater, go right
        else:
          if not self.right:
            return False
          else:
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
          ## iterative solution

          # current_tree_root = self
          # while current_tree_root.right:
          #   current_tree_root = current_tree_root.right

          # return current_tree_root.value

          ## recursive solution

          # if we can go right, go right
          # return when we can't go right anymore
          if not self.right:
            return self.value

          max_value = self.right.get_max()

          return max_value



    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, callback):
        if self == None:
          return

        # call the function
        callback(self.value)

        # if left is not None, go left
        if self.left:
          self.left.for_each(callback)

        # if right is not None, go right
        if self.right:
          self.right.for_each(callback)


    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):

        if node.left:
          self.in_order_print(node.left)

        print(node.value)

        if node.right:
          self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # create queue and enqueue the root node of the BST
        queue = Queue()
        queue.enqueue(node)

        # loop until the queue is empty
        while queue.len() > 0:

          # grab the current node in the queue
          current_node = queue.dequeue()

          # print the first item and enqueue any children
          print(current_node.value)

          if current_node.left:
            queue.enqueue(current_node.left)

          if current_node.right:
            queue.enqueue(current_node.right)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # creat stack and push the node
        stack = Stack()
        stack.push(node)

        # loop until the stack is empty
        while stack.len() > 0:
          current_node = stack.pop()

          # print the last item and push any children
          print(current_node.value)

          if current_node.left:
            stack.push(current_node.left)

          if current_node.right:
            stack.push(current_node.right)


    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        if node:
          print(node.value)

        if node.left:
          self.pre_order_dft(node.left)

        if node.right:
          self.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node.left:
          self.post_order_dft(node.left)

        if node.right:
          self.post_order_dft(node.right)

        print(node.value)
