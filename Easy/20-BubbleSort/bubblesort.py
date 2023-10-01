
#   Write a function that takes in an array of integers and returns a sorted
#   version of that array. Use the Bubble Sort algorithm to sort the array.
#
#   Sample Input:
#       array = [8, 5, 2, 9, 5, 6, 3]
#   Sample Output:
#       [2, 3, 5, 5, 6, 8, 9]
#
# Iterative Solution
# O(n^2) time | O(1) space
def bubbleSort(array):

    isSorted = False # assume array is not sorted
    counter = 0 # counter to keep track of how many times we've gone through the array

    while not isSorted: # while array is not sorted
        isSorted = True # assume array is sorted
        for i in range(0, len(array) - 1 - counter): # iterate through array from 0 to len(array) - 1 - counter
            if array[i] > array[i+1]: # if current element is greater than next element
                array[i] , array[i+1] = array[i+1], array[i] # swap elements
                isSorted = False # array is not sorted yet because we had to swap elements to sort them 
                
        counter += 1 # increment counter to keep track of how many times we've gone through the array 
            
    return array  # return sorted array

# Example input:
array = [8, 5, 2, 9, 5, 6, 3]
# Example output:
output = bubbleSort(array)
print(output)
# expected output = [2, 3, 5, 5, 6, 8, 9]

        
