
#   Write a function that takes in a non-empty array of integers that are sorted
#   in ascending order and returns a new array of the same length with the squares
#   of the original integers also sorted in ascending order.

# sample input = [1, 2, 3, 5, 6, 8, 9]
# sample output = [1, 4, 9, 25, 36, 64, 81]

def sortedSquaredArrayBruteforce(array):

    # Write your code here
    if(not array):
        return
    
    res = []
    for element in array:
        res.append(element**2)

    sortedArray = sorted(res)
    return sortedArray


def sortedSquaredArrayLinearTime(array):
    # start = array[0]
    # end = array[-1]
    smallerValueIdx = 0
    largerValueIdx = len(array) - 1
    sortedArray = [0 for _ in array]



    for index in reversed(range(len(array))):

        smallerValue = array[smallerValueIdx]
        largerValue = array[largerValueIdx]

        if (abs(smallerValue) > abs(largerValue)):
            smallerValueIdx = smallerValueIdx + 1
            sortedArray[index] = smallerValue * smallerValue

        else:
            largerValueIdx = largerValueIdx - 1
            sortedArray[index] = largerValue * largerValue

    return sortedArray

input = [-7, -5, -4, 3, 6, 8, 9]
sortedBruteForce = sortedSquaredArrayBruteforce(input)
print(sortedBruteForce)

sortedLinear = sortedSquaredArrayLinearTime(input)
print(sortedLinear)


## Brute force method
# Generate all squares of the input array, then sort the array
# Time complexity O(nlogn), space ccomplexity O(n)


## Linear time complexity method - Hint is when we get an input that is already sorted by default
#  Use two pointers to keep track of the smallest and largest values in the input
#  array. Compare the absolute values of these smallest and largest values,
#  square the larger absolute value, and place the square at the end of the
#  output array, filling it up from right to left. Move the pointers accordingly,
#  and repeat this process until the output array is filled.
