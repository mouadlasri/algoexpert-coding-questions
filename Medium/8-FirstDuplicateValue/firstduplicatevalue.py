
#  Given an array of integers between 1 and n, inclusive, where n is the length of the array,
#  write a function that returns the first integer that appears more than once (when the array is read from left to right).
#  In other words, out of all the integers that might occur more than once in the input array, your function should return the one whose first duplicate value has the minimum index.
#  If no integer appears more than once, your function should return -1.
#  Note that you're allowed to mutate the input array.
#
#  Sample Input
#  array = [2, 1, 5, 2, 3, 3, 4]
#  Sample Output
#  2 // 2 is the first integer that appears more than once.
#  3 also appears more than once, but the second 3 appears after the second 2.
#


# Solution 1
# Time: O(n) | Space: O(n)
###############################
# def firstDuplicateValue(array):
#     # Write your code here.
#     seen = set()
#     for i in range(len(array)):
#         if array[i] in seen:
#             return array[i]
#         else:
#             seen.add(array[i])
#     return -1
#
# # Example input:
# array = [2, 1, 5, 2, 3, 3, 4]
# print(firstDuplicateValue(array))
#
# # Output: 2

# Solution 2
# Time: O(n) | Space: O(1)
###############################

def firstDuplicateValue(array):
    
    # Explanation: 
    # We can use the array itself as a hash table.
    # We can do this by using the values of the array as indices.
    # We can then mark the values at those indices as negative.
    # If we come across a value that is already negative, then we know that we have seen that value before.
    # We can then return that value.
    # If we don't find a value that is negative, then we know that there are no duplicates.
    # We can then return -1.
    # Note: We can use the absolute value of the value at the current index as the index to mark as negative.
    # This is because we know that the values in the array are between 1 and n, inclusive, where n is the length of the array.
    # This means that the values in the array are valid indices.
    
    for i in range(len(array)): 
        absValue = abs(array[i])
        if array[absValue - 1] < 0: # Checking if the value at the current index is negative
            return absValue # Returning the value at the current index
        else: # If the value at the current index is not negative then we mark it as negative by multiplying it by -1 
            array[absValue - 1] *= -1 # Marking the value at the current index as negative
    return -1


# Example input:
array = [2, 1, 5, 2, 3, 3, 4]
print(firstDuplicateValue(array))

# Output: 2
