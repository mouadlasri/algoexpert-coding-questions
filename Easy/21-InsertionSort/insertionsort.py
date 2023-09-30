
#   Write a function that takes in an array of integers and returns a sorted
#   version of that array. Use the Insertion Sort algorithm to sort the array.
#
#   If you're unfamiliar with Insertion Sort, we recommend watching the Conceptual
#   Overview section of this question's video explanation before starting to code.
#
#   Sample Input:
#       array = [8, 5, 2, 9, 5, 6, 3]
#  Sample Output:
#       [2, 3, 5, 5, 6, 8, 9]

# Solution 1
# O(n^2) time / O(1) space

# Insertion Sort explanation:
# The idea behind insertion sort is that you divide the array into two portions: a sorted portion and an unsorted portion.
# Initially, the sorted portion is empty and the unsorted portion is the entire array.
# Then, you take the first element in the unsorted portion and insert it into the correct position in the sorted portion.
# You do this by comparing the current element to the previous element in the sorted portion.
# If the current element is smaller than the previous element, you swap them.
# You keep doing this until the current element is in its correct position.
# Then, you move on to the next element in the unsorted portion and repeat the process.
# You keep doing this until the unsorted portion is empty and the sorted portion is the entire array.


def insertionSort(array):
    for i in range(1, len(array)): 
        j = i    
        while j > 0 and array[j] < array[j-1]: # each iteration of this while loop will move the current element to its correct position in the sorted portion of the array
            swap(j, j-1, array) # swap current element with previous element
            j -= 1 # decrement j to move to the next element in the sorted portion of the array

    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

# Sample input: [8, 5, 2, 9, 5, 6, 3]
array = [8, 5, 2, 9, 5, 6, 3]
print(insertionSort(array)) # output: [2, 3, 5, 5, 6, 8, 9]

