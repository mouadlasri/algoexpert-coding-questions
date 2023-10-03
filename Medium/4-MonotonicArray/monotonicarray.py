
#  Write a function that takes in an array of integers and returns a boolean
#  representing whether the array is monotonic.
#  An array is said to be monotonic if its elements, from left to right, are entirely non-increasing or entirely non-decreasing.
#  Non-increasing elements aren't necessarily exclusively decreasing; they simply don't increase. Similarly, non-decreasing elements aren't necessarily
#   exclusively increasing; they simply don't decrease.
#  Note that empty arrays and arrays of one element are monotonic.


#  Sample Input
#  array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
#  Sample Output
#  true

def isMonotonic(array):
    
    isNonDecreasing = True
    isNonIncreasing = True

    for i in range(1, len(array)):
        if array[i] < array[i-1]:
            IsNonDecreasing = False
        if array[i] > array[i-1]:
            isNonIncreasing = False

    return isNonDecreasing or isNonIncreasing

# Time: O(n)
# Space: O(1)

# Input example
array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]

print(isMonotonic(array))

# Output
# true
