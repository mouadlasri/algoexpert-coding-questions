# You're given a Node class that has a name and an array of optional children nodes.
# When put together, nodes form an acyclic tree-like structure.
# Implement the depthFirstSearch method on the Node class, which takes in an empty
# array, traverses the tree using the Depth-first Search approach (specifically
# navigating the tree from left to right), stores all of the nodes' names in the
# input array, and returns it.

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self
    
    def depthFirstSearch(self, array):
        # Write your code here.
        array.append(self.name)

        for child in self.children:
            child.depthFirstSearch(array)
        return array
        

# Sample input
# graph =
#           A
#         / | \
#        B  C  D
#       / \   / \
#      E   F G   H
#         / \ \
#        I   J K
#
# Sample output (DFS): ["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"]

graph = Node("A")
graph.addChild("B").addChild("C").addChild("D")
graph.children[0].addChild("E").addChild("F")
graph.children[2].addChild("G").addChild("H")
graph.children[0].children[1].addChild("I").addChild("J")
graph.children[2].children[0].addChild("K")

print(graph.depthFirstSearch([]))
