# You're given a 2D array of integers matrix
# Write a function that returns the transpose of the matrix.
# The transpose of a matrix is a flipped version of the original matrix across
# its main diagonal (which runs from top-left to bottom-right); it switches
# the row and column indices of the original matrix.

# For example:
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# output = [
#     [1, 4, 7],
#     [2, 5, 8],
#     [3, 6, 9]
# ]

def transposeMatrix(matrix):
    # Write your code here.
    numberRows = len(matrix) # number of rows in matrix
    numberCols = len(matrix[0]) # number of columns in matrix

    newMatrix = []
    newRow = []
    for i in range(numberCols):
        newRow = []
        for j in range(numberRows):
            newRow.append(matrix[j][i])
        newMatrix.append(newRow)
    
    return newMatrix

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

result = transposeMatrix(matrix)

print(result)


