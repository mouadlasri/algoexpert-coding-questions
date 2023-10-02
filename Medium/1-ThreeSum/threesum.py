
#   Write a function that takes in a non-empty array of distinct integers and an
#   integer representing a target sum. The function should find all triplets in
#   the array that sum up to the target sum and return a two-dimensional array of
#   all these triplets. The numbers in each triplet should be ordered in ascending
#   order, and the triplets themselves should be ordered in ascending order with
#   respect to the numbers they hold.
#
#   If no three numbers sum up to the target sum, the function should return an
#   empty array.
#
#   Sample Input:
#       array = [12, 3, 1, 2, -6, 5, -8, 6]
#       targetSum = 0
#   Sample Output:
#       [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
#       // the triplets could be ordered differently

def threeNumberSum(array, targetSum):

    pairs = []
    
    array.sort() # sort the array in ascending order

    for i in range(0, len(array)):
        l = i + 1
        r = len(array) - 1
        
        while l < r:
            
            currentSum = array[i] + array[l] + array[r]

            if currentSum < targetSum: # we have to move the left pointer closer to the right side (to get a bigger sum)
                l = l + 1
            elif currentSum > targetSum: # we have to move the right pointer closer to the left side (to get a smaller sum)
                r = r - 1
            else: # found the target sum
                pairs.append([array[i], array[l], array[r]])
                l = l + 1
                r = r - 1

    return pairs
                
    
# Time Complexity: O(n^2)
# Space Complexity: O(n)

# Input example
array = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 0

print(threeNumberSum(array, targetSum))
# Output: [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
