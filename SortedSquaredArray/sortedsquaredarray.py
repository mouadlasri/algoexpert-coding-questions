
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

input = [1, -62, 3, 5, 6, 8, 9]
sorted = sortedSquaredArrayBruteforce(input)
print(sorted)

# Brute force method
# Generate all squares of the input array, then sort the array
# Time complexity O(nlogn), space ccomplexity O(n)