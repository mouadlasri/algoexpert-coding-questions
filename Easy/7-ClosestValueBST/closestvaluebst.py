# You can assume that there will only be one closest value.
# You can assume that there will only be one closest value.

# Sample Input:
#          10
#        /     \
#       5      15
#     /   \   /   \
#    2     5 13   22
#  /           \
# 1            14

# Sample Output:
# 13

def findValueHelper(tree, target, closest):

    if(tree is None):
        return closest

    if abs(target - tree.value) < abs(target - closest):
        closest = tree.value

    if target > tree.value:
        # go to right subtree, any node on the left subtree will increase the distance
        return findValueHelper(tree.right, target, closest)

    elif target < tree.value:
        # go to left subtree, any node on the right subtree will increase the distance
        return findValueHelper(tree.left, target, closest)
        
    else: 
        return closest

    


def findClosestValueInBst(tree, target):
    return findValueHelper(tree, target, float("inf"))


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Example:

root = BST(10)
root.left = BST(5)
root.left.left = BST(2)
root.left.left.left = BST(1)
root.left.right = BST(5)
root.right = BST(15)
root.right.left = BST(13)
root.right.left.right = BST(14)
root.right.right = BST(22)

target = 12

print(findClosestValueInBst(root, target))
#
# Sample Output:
# 13
