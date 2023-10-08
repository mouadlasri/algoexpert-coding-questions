
# You're given an unordered list of unique integers nums in the range [1, n], where n represents the length of nums + 2.
# This means that two numbers in this range are missing from the list
# Write a function that takes in nums and returns the two missing numbers in sorted order.

# Input: [1, 4, 3]
# Output: [2, 5] // 2 and 5 are missing from the list

# Time complexity: O(n) because we use max instead of sorting
# Space complexity: O(n)
def missingNumbers(nums):
    if nums is None:
        return []
        
    length = len(nums) + 2
    numsSet = set(nums)
    results = []

    for i in range(1, length+1):
        if i not in numsSet:
            results.append(i)

    return results
            
    
# Input: [1, 4, 3]
nums = [1, 4, 3]
print(missingNumbers(nums))
# Output: [2, 5] // 2 and 5 are missing from the list
