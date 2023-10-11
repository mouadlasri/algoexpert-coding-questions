
#   Write a function that takes in two strings and returns the minimum number of
#   edit operations that need to be performed on the first string to obtain the
#   second string.
#
#   There are three edit operations: insertion of a character, deletion of a character,
#   and substitution of a character for another.
# 
#   Sample Input:
#   str1 = "abc"
#   str2 = "yabd"
#
#   Sample Output:
#   2 // insert "y"; substitute "c" for "d"
#
#   Solution:
#   We can solve this problem using dynamic programming.
#   We will create a matrix of size (len(str1) + 1) x (len(str2) + 1).
#   The rows of the matrix will represent the characters of str1 and the columns will represent the characters of str2.
#   We will start filling the matrix from the top left corner.
#   The first row and the first column will be filled with numbers from 0 to len(str1) and len(str2) respectively.
#   The rest of the cells will be filled as follows:
#   If the character of str1 at the current row is equal to the character of str2 at the current column,
#   we will fill the current cell with the value in the cell directly above it.
#   Otherwise, we will fill it with 1 plus the minimum of the values in the cells directly above, left, and above-left.
#   Once the matrix is filled, the answer will be at the bottom right corner of the matrix.

# O(n*m) time | O(n*m) space
# where n and m are the lengths of both strings
def levenshteinDistance(str1, str2):
    # create edits 2D matrix (E matrix)
    edits = [[x for x in range(len(str1) + 1)] for y in range(len(str2) + 1)]
    # [0, 1, 2, 3, 4 ...]   str2 rows
    #  1
    #  2
    #  3
    #  4
    # str1 columns
    
    for i in range(1, len(str2) + 1):
        edits[i][0] = edits[i-1][0] + 1 # first column that goes from 0 to the len of str1

    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            # apply formula:
            # if both letters we're comparing are  equal (not the same letters)
            # check the surrounding 3 boxes (up,  and diagonal) values
            # pick the minimum of those three values and add 1 to them
            # if str1[r-1] == str2[c-1]: E[r][c] = E[r-1][c-1]
            # in this case, we check r-1 index because we shifted our array by one in the matrix since we added an empty character string
            if(str2[i-1] == str1[j-1]):
                edits[i][j] = edits[i-1][j-1]
    
            # if both letters are not equal, choose diagobal value
            # if str1[r-1] == str2[c-1]: E[r][c] = 1+ min(E[r][c-1], E[r-1][c], E[r-1][c-1])
            else:
                edits[i][j] = 1 + min(edits[i][j-1], edits[i-1][j-1], edits[i-1][j])

    return edits[len(str2)][len(str1)] # or return edits[-1][-1] ie the final value in the matrix
            

str1 = "abc"
str2 = "yabd"
print(levenshteinDistance(str1, str2))
# 2 // insert "y"; substitute "c" for "d"