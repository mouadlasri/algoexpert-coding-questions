# Write a BFS algorithm to apply on a graph with any external libraries
# Input: graph, source node
# Output: list of nodes in the order of BFS
# Assumption: graph is a dictionary of nodes and their neighbors
#             source is a node in the graph
# Complexity: O(V+E) time, O(V) space
#             V is the number of nodes in the graph


def bfs(graph, source):
    # Initialize result list
    result = []
    # Initialize a queue
    queue = []
    # Initialize a set of visited nodes
    visited = set()
    # Add source to the queue
    queue.append(source)
    # Add source to the visited set
    visited.add(source)
    # While queue is not empty

    while queue:
        # Pop the first node in the queue
        node = queue.pop(0)

        # Add the node to the result list
        result.append(node)

        # For each neighbor of the node
        for neighbor in graph[node]:
            # If the neighbor is not visited
            if neighbor not in visited:
                # Add the neighbor to the queue
                queue.append(neighbor)
                # Add the neighbor to the visited set
                visited.add(neighbor)


    return result


# Test
graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}

print(bfs(graph, 'A'))

