# Write a function that takes in a potentially invalid Binary Search Tree (BST) and returns a boolean representing whether the BST is valid.
#
# Each BST node has an integer value, a left child node, and a right child node. 
# A node is said to be a valid BST node if and only if it satisfies the BST property:
# - its value is strictly greater than the values of every node to its left;
# - its value is less than or equal to the values of every node to its right;
# - and its children nodes are either valid BST nodes themselves or None / null.
#
# A BST is valid if and only if all of its nodes are valid BST nodes.

# Sample Input:
# tree =   10
#        /     \
#       5      15
#     /   \   /   \
#    2     5 13   22
#   /           \
#  1            14

# Sample Output:
# true

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# main function to validate a BST
def validateBst(tree):
    return validateBstHelper(tree, float("-inf"), float("inf"))


# helper function to validate a BST recursively using the BST property (see above) and the min/max values of the tree nodes
# minValue is the value of the leftmost node in the tree
# maxValue is the value of the rightmost node in the tree
def validateBstHelper(tree, minValue, maxValue):
    if tree is None:
        return False
    
    if tree.value < minValue or tree.value >= maxValue:
        return False
    
    # leftIsValid is True if the left subtree is valid, False otherwise
    # Why do we send tree.left, minValue and tree.value as parameters to the recursive call?
    # Because the left subtree must be smaller than the current node, but it can be larger than the parent node

    leftIsValid = validateBstHelper(tree.left, minValue, tree.value)

    # rightIsValid is True if the right subtree is valid, False otherwise
    # Why do we send tree.right, tree.value and maxValue as parameters to the recursive call?
    # Because the right subtree must be larger than the current node, but it can be smaller than the parent node
    return leftIsValid and validateBstHelper(tree.right, tree.value, maxValue)
