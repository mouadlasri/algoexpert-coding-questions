#   You're given a list of integers
#   Write a function that returns a boolean representing whether there exists a zero-sum subarray of nums (the input list)

#   A zero-sum subarray is any subarray where all of the values add up to zero.
#   A subarray is any contiguous section of the array. For the purposes of this
#   problem, a subarray can be as small as one element and as long as the
#   original array.
  
# Sample Input:
#   nums = [-5, -5, 2, 3, -2]

# Sample Output:
#   true // [-5, 2, 3] has a sum of 0
 
def zeroSumSubarray(nums):
    sums = set() # set of all the sums of all the subarrays we've seen so far
    sums.add(0)

    currentSum = 0
    
    for num in nums:
        currentSum += num
        
        # if we've seen this sum before, then there exists a zero-sum subarray in the array because 
        # the sum of the subarray from the first time we saw this sum to the current sum is 0 
        # ie: the subarray from the first time we saw this sum to the current sum is a zero-sum subarray (currentSum - firstTimeWeSawThisSum = 0)
        # (because the sum of the subarray from the first time we saw this sum to the current sum is the current sum minus the first time we saw this sum,
        #  which is 0)
        # therefore, the range of the subarray from the first time we saw this sum (exclusive) to the current sum (inclusive) is a zero-sum subarray 
        # example: nums = [-5, -5, 2, 3, -2]
    
        if currentSum in sums:  
            return True
            
        sums.add(currentSum) # add the current sum to the set of sums we've seen so far (because we haven't seen this sum before)

    return False
   
            
        


