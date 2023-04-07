
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