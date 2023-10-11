# Write a BST class for a Binary Search Tree. The class should support:
# - Inserting values with the insert method.
# - Removing values with the remove method; this method should only remove the first instance of a given value.
# - Searching for values with the contains method.
#
# Note that you can't remove value from a single-node tree. In other words, calling the remove method on a single-node tree should simply not do anything. 
# Each BST node has an integer value, a left child node, and a right child node. 
# A node is said to be a valid BST node if and only if it satisfies the BST property:
# 
# its value is strictly greater than the values of every node to its left;
# its value is less than or equal to the values of every node to its right;
# and its children nodes are either valid BST nodes themselves or None / null.
#
# Sample Usage:
# // Assume the following BST has already been created:
#          10
#        /     \
#       5      15
#     /   \   /   \
#    2     5 13   22
#   /           \
#  1            14
#
# // All operations below are performed sequentially.
# insert(12):   10
#            /     \
#           5      15
#         /   \   /   \
#        2     5 13   22
#       /       /  \
#      1       12   14
#
# remove(10):   12
#            /     \
#           5      15
#         /   \   /   \
#        2     5 13   22
#       /           \
#      1            14

# contains(15): true


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        currentNode = self
        while True:
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left
            else: # if value > currentNode.value ie the new node has to be inserted on the right side of the current node
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right
                    
        return self

    def contains(self, value):
        currentNode = self

        while currentNode is not None:
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            else: # found the value
                return True

        return False

    def remove(self, value, parentNode=None):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value: # go to left subarray
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value: # go to right subarray
                parentNode = currentNode
                currentNode = currentNode.right
            else: # if value to remove is found (node to remove is found)
                # first subcase: dealing with a node that has two children nodes
                # find smallest value ion the right subtree to replace it with .
                if currentNode.left is not None and currentNode.right is not None:
                    currentNode.value = currentNode.right.getMinValue()  # currentNode.value = smallest value of right subtree
                    # remove the current node
                    currentNode.right.remove(currentNode.value, currentNode) # pass value and parent node

                # special case, if it's the root node that we have to remove
                elif parentNode is None:
                    if currentNode.left is not None:
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right
                        currentNode.left = currentNode.left.left
                    elif currentNode.right is not None:
                        currentNode.value = currentNode.right.value
                        currentNode.left = currentNode.right.left
                        currentNode.right = currentNode.right.right
                    else:
                        # this is a single-node tree; do nothing
                        pass
                        
                # if currentNode is itself a left child or right child
                elif parentNode.left == currentNode:
                    parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
                elif parentNode.right == currentNode:
                    parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right
                break
        
        return self
                
    def getMinValue(self):
        currentNode = self
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode.value



