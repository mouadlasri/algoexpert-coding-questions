# You're given a list of edges representing an unweighted, directed graph with at least one node.
# Write a function that returns a boolean representing whether the given graph contains a cycle.
#
# For the purpose of this question, a cycle is defined as any number of vertices, including just one vertex, that are connected in a closed chain.
# A cycle can also be defined as a chain of at least one vertex in which the first vertex is the same as the last.
#
# The given list is what's called an adjacency list, and it represents a graph. The number of vertices in the graph is equal to the length of
# edges, where each index i in edges contains vertex i's outbound edges, in no particular order.
#
# Each individual edge is represented by a positive integer that denotes an index (a destination vertex) in the list that
# this vertex is connected to. Node that these edges are directed, meaning that you can only traveal from a particular vertex to its destination,
# not the other way around *unless the destination vertex itself has an outbound edge to the original vertex.
#
# Also note that this graph may contain self-loops. A self-loop is an edge that has the same destination and origin; in other words, it's an edge
# that connects a vertex to itself. For the purpose of this question, a self-loop is considered a cycle.
#


def cycleInGraph(edges):
    # get number of nodes in the graph (which is the length of the edges adjacency list)
    numberOfNodes = len(edges)

    # initialize visited and currentlyInStack arrays which are used to keep track of nodes that have been visited 
    visited = [False for _ in range(numberOfNodes)]

    # initialize currentlyInStack array which is used to keep track of nodes that are currently in the stack 
    # (which means that they are part of the current path)
    currentlyInStack = [False for _ in range(numberOfNodes)]

    # loop through all nodes
    for node in range(numberOfNodes):
        if visited[node] == True: # if node has been visited, don't visit again, skip it and continue the loop
            continue

        # if node has not been visited, do a DFS on it (by doing a DFS on its neighbors)
        containsCycle = isNodeInCycle(edges, node, visited, currentlyInStack)

        if containsCycle == True:
            return True


    # no cycle found
    return False


def isNodeInCycle(edges, node, visited, currentlyInStack):

    # mark the node as visited and add it to currentlyInStack
    visited[node] = True

    # add the node to the currentlyInStack array because we are currently doing a DFS on it (and it is part of the current path)
    currentlyInStack[node] = True

    # check the neighbors of this Node
    neighbors = edges[node]

    for neighbor in neighbors:
        if visited[neighbor] == False: # if the neighbor was not already visited before
            # do a DFS on the neighbor Node
            containsCycle = isNodeInCycle(edges, neighbor, visited, currentlyInStack)

            if containsCycle == True:
                return True
        
        elif currentlyInStack[neighbor] == True:
            return True
        
    # remove the node from the currentlyInStack array because we are done doing a DFS on it (and it is no longer part of the current path) 
    currentlyInStack[node] = False

    return False