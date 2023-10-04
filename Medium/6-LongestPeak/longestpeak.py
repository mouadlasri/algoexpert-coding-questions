
#   Write a function that takes in an array of integers and returns the length of
#   the longest peak in the array.
#
#   A peak is defined as adjacent integers in the array that are strictly
#   increasing until they reach a tip (the highest value in the peak), at which
#   point they become strictly decreasing. At least three integers are required to
#   form a peak.
#
#   For example, the integers 1, 4, 10, 2 form a peak, but the integers 4, 0, 10 don't and neither do the integers
#   1, 2, 2, 0. Similarly, the integers 1, 2, 3 don't form a peak because there aren't any strictly decreasing integers after the 3.
#
#   Sample Input
#   array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
#   Sample Output
#   6 // 0, 10, 6, 5, -1, -3
#

# Time: O(n)
# Space: O(1)

def longestPeak(array):

    longestPeakLength = 0
    i = 1

    while i < len(array) - 1:
        isPeak = array[i-1] < array[i] and array[i] > array[i+1]
        if not isPeak: # if we didn't reach a peakj
            i+= 1
            continue

        # if we find a peak, we need to expand through the left and right to calculate the length of the peak
        # on both sides

        # left side
        leftIdx = i - 2 # start from peak-2 index
        while leftIdx >= 0 and array[leftIdx] < array[leftIdx + 1]:
            leftIdx = leftIdx - 1

        # right side
        rightIdx = i + 2 # start from peak+2 index
        while rightIdx < len(array) and array[rightIdx] < array[rightIdx - 1]:
            rightIdx = rightIdx + 1

        # calcualte the current peak length
        currentPeakLength = rightIdx - leftIdx - 1
        
        # update longestPeakLength with the biggest of the two values
        longestPeakLength = max(longestPeakLength, currentPeakLength)
        currentPeakLength 

        # iterate through the array and skip the rightIdx that we alreayd iterated over since we 
        i = rightIdx 
        
        
    return longestPeakLength
        
         
        
            
    
# Input example
array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]

print(longestPeak(array))

# Output
# 6
