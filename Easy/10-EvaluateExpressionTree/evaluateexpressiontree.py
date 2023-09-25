

# You're given a binary expression tree. Write a function to evaluate
# this tree mathematically and return a single resulting integer.

# All leaf nodes in the tree represent operands, which will always be positive
# integers. All of the other nodes represent operators. There are 4 operators
# supported, each of which is represented by a negative integer:

# -1: Addition
# -2: Subtraction
# -3: Division
# -4: Multiplication

# You can assume the tree will always be a valid expression tree. Each
# operator also works as a grouping symbol, meaning the bottom of the tree is
# always evaluated first, regardless of the operator.
  
# Input 
#       -1
#      / \
#     -2   -3
#    / \ / \
#   -4  2 8 3
#  / \
# 2   3

# Output: 6 : (((2 * 3) - 2) + (8 / 3))

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left  = left
        self.right = right

def evaluateExpressionTree(root):
    if (root.value >= 0):
        return root.value
    
    leftValue = evaluateExpressionTree(root.left)
    rightValue = evaluateExpressionTree(root.right)

    if (root.value == -1):
        return leftValue + rightValue
    elif (root.value == -2):
        return leftValue - rightValue
    elif (root.value == -3):
        return int(leftValue / rightValue)
   
    return leftValue * rightValue
    


# Sample input
root = BinaryTree(-1)
root.left = BinaryTree(-2)
root.right = BinaryTree(-3)
root.left.left = BinaryTree(-4)
root.left.right = BinaryTree(2)
root.right.left = BinaryTree(8)
root.right.right = BinaryTree(3)
root.left.left.left = BinaryTree(2)
root.left.left.right = BinaryTree(3)

# Expected output: 6 : (((2 * 3) - 2) + (8 / 3))
result = evaluateExpressionTree(root)

print(result)
