
#   Write a function that takes in an n x m two-dimensional array (that can be
#   square-shaped when n == m) and returns a one-dimensional array of all the
#   array's elements in spiral order.
#
#   Spiral order starts at the top left corner of the two-dimensional array, goes
#   to the right, and proceeds in a spiral pattern all the way until every
#   element has been visited.
#
#   Sample Input
#   array = [
#     [1,   2,  3, 4],
#     [12, 13, 14, 5],
#     [11, 16, 15, 6],
#     [10,  9,  8, 7],
#   ]
#   Sample Output
#   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# 
#   Time: O(n)

def spiralTraverse(array):
    result = []
    startRow, endRow = 0, len(array) - 1
    startCol, endCol = 0, len(array[0]) - 1

    while startRow <= endRow and startCol <= endCol:
        # traverse top border (left to right)
        for col in range(startCol, endCol + 1): # endCol incluside
            result.append(array[startRow][col]) 

        # traverse right border (top to bottom)
        for row in range(startRow + 1, endRow + 1): # startRow + 1 is to avoid counting the value twice with previous loop
            result.append(array[row][endCol])

        # traverse bottom border (right to left)
        for col in reversed(range(startCol, endCol)):
            # handle edge case when there is a single row in the middle of the matrix.
            if startRow == endRow:
                break
            result.append(array[endRow][col])

        # traverse left border (bottom to top)
        for row in reversed(range(startRow + 1, endRow)):
            # handle edge case when there is a single column in the middle of the matrix
            if startCol == endCol:
                break
            result.append(array[row][startCol])

        startRow = startRow + 1
        endRow = endRow - 1
        
        startCol = startCol + 1 
        endCol = endCol - 1

    return result
        
            
# Input example
array = [
    [1,   2,  3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10,  9,  8, 7],
]

print(spiralTraverse(array))

# Expected output
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]