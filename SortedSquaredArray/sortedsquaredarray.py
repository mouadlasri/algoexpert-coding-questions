
#   Write a function that takes in a non-empty array of integers that are sorted
#   in ascending order and returns a new array of the same length with the squares
#   of the original integers also sorted in ascending order.

# sample input = [1, 2, 3, 5, 6, 8, 9]
# sample output = [1, 4, 9, 25, 36, 64, 81]

def sortedSquarredArray(array):
    # Write your code here
    if(not array):
        return
  
    res = []
    # get first element squared and push it to res
    for index in range(0, len(array)):
        smallest = min(array)
        largest = max(array)

        if(abs(largest) > abs(smallest)):
            square = largest * largest
        else:
            square = smallest * smallest

        res.insert(0, square)
        
        array.pop(array.index(largest))
        
    return res


# Hint

#   Use two pointers to keep track of the smallest and largest values in the input
#   array. Compare the absolute values of these smallest and largest values,
#   square the larger absolute value, and place the square at the end of the
#   output array, filling it up from right to left. Move the pointers accordingly,
#   and repeat this process until the output array is filled.
