
#   Write a function that takes in a Binary Tree and returns a list of its branch
#   sums ordered from leftmost branch sum to rightmost branch sum.

#   A branch sum is the sum of all values in a Binary Tree branch. A Binary Tree
#   branch is a path of nodes in a tree that starts at the root node and ends at
#   any leaf node.

# sample input
# tree =     1
#         /     \
#        2       3
#      /   \    /  \
#     4     5  6    7
#   /   \  /
#  8    9 10

# sample output
# [15, 16, 18, 10, 11]

# This is the class of the input root. Do not edit it.
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def dfsSearch(root, currentSum, results):

    if(root is None):
        return
    
    if(root is not None):
        currentSum = currentSum + root.value

        dfsSearch(root.left, currentSum, results)
        dfsSearch(root.right, currentSum, results)
        

        if(root.left is None and root.right is None):
            results.append(currentSum)
            

def branchSums(root):
    # Write your code here.
    currentSum = 0

    results = []

    dfsSearch(root, currentSum, results)
    print(results)
    
    return results
    

# Example:

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
  

branchSums(root)


