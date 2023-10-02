
#   Write a function that takes in two non-empty arrays of integers, finds the
#   pair of numbers (one from each array) whose absolute difference is closest to
#   zero, and returns an array containing these two numbers, with the number from
#   the first array in the first position.
#
#   Note that the absolute difference of two integers is the distance between
#   them on the real number line. For example, the absolute difference of -5 and 5
#   is 10, and the absolute difference of -5 and -4 is 1.
#
#   You can assume that there will only be one pair of numbers with the smallest
#   difference.

def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    # absolute difference = |y-x|

    arrayOne.sort()
    arrayTwo.sort()

    oneIdx, twoIdx = 0, 0

    pair = []

    smallest = float("inf")
    
    while oneIdx < len(arrayOne) and twoIdx < len(arrayTwo):
        
        numOne, numTwo = arrayOne[oneIdx], arrayTwo[twoIdx]

        currentDiff = abs(numOne - numTwo)

        if currentDiff == 0:
            pair = [numOne, numTwo]
            break
          
        if currentDiff < smallest:
            smallest = currentDiff
            pair = [numOne, numTwo]

        if numOne < numTwo:
            oneIdx = oneIdx + 1
        else:
            twoIdx = twoIdx + 1

    return pair
 
    

# Time Complexity: O(nlog(n) + mlog(m)) where n is the length of arrayOne and m is the length of arrayTwo

# Space Complexity: O(1)

                
# Input example
arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]

print(smallestDifference(arrayOne, arrayTwo))
# Output: [28, 26]

    