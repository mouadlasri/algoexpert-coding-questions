
#   Write a function that takes in a sorted array of integers as well as a target
#   integer. The function should use the Binary Search algorithm to determine if
#   the target integer is contained in the array and should return its index if it
#   is, otherwise -1.
#
#   Sample Input:
#       array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
#       target = 33
#   Sample Output:
#       3
#
# Solution 1: Recursive Solution
# O(log(n)) time | O(log(n)) space
def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array) - 1)

def binarySearchHelper(arr, target, left, right):
    if left > right:
        return -1
    
    middle = (left + right) // 2

    potentialMatch = arr[middle]

    if target == potentialMatch: # found target
        return middle
    elif target < potentialMatch: # target is in left half
        return binarySearchHelper(arr, target, left, middle - 1)
    else:   # target is in right half
        return binarySearchHelper(arr, target, middle + 1, right)
    
# Example input:
array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
target = 33
# Example output:
output = binarySearch(array, target)
print(output)
# expected output = 3