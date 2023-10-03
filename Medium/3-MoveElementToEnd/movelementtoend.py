
#   You're given an array of integers and an integer. Write a function that moves
#   all instances of that integer in the array to the end of the array and returns
#   the array.
#
#   The function should perform this in place (i.e., it should mutate the input
#   array) and doesn't need to maintain the order of the other integers.
#
#   Sample Input:
#       array = [2, 1, 2, 2, 2, 3, 4, 2]
#       toMove = 2
#   Sample Output:
#       [1, 3, 4, 2, 2, 2, 2, 2] // the numbers 1, 3, and 4 could be ordered differently

# Solution: O(n) time | O(1) space

def moveElementToEnd(array, toMove):
    # Write your code here.

    if array is None:
        return array
        
    left = 0 # left
    right = len(array) - 1 # right

    while left < right:
        if array[left] == toMove and array[right] is not toMove: # found element to move to the end of the array
            swap(left, right, array) # swap both elements
            left = left + 1 # update left pointer to the next element from the left
            right = right - 1 # update right pointer to the next element from the right because the previous element got swapped (already holds toMove value)
        elif array[left] is not toMove: # iterate through the array from the left side 
            left = left + 1 
        elif array[right] is toMove: # if array[left] is equal to toMove but not array[right], move right pointer until we find a toMove value
            right = right - 1
            
    return array


def swap(left, right, array):
    array[left], array[right] = array[right], array[left]
    

# Input example:
array = [2, 1, 2, 2, 2, 3, 4, 2]
toMove = 2

# Output example:
print(moveElementToEnd(array, toMove)) # [1, 3, 4, 2, 2, 2, 2, 2] // the numbers 1, 3, and 4 could be ordered differently

    
