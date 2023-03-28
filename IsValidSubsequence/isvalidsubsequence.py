
#   Given two non-empty arrays of integers, write a function that determines
#   whether the second array is a subsequence of the first one.

#   A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array but that are in the same order as they appear in the array.
#   For instance, the numbers [1, 3, 4] form a subsequence of the array [1, 2, 3, 4], and so do the numbers [2, 4]

#   Note
#   that a single number in an array and the array itself are both valid
#   subsequences of the array.

def isValidSubsequence(array, sequence):
    # Write your code here.

    # idea
    # 1- check if seq is in array and add it to a new array
    # 2- slice the list to eliminate all values before the element's index that we found.
    # The goal of slicing is to avoid adding elements to temp array whose index comes before the existing elements
    # 3- compare temp and seuqnce at the end
    
    temp = []

    # if sequence and array are equal
    if(sequence == array):
            return True
        
    for  seq in sequence:
        if(seq in array ):
            temp.append(seq) # append it to end of list
            array = array[array.index(seq)+1:] # slice the list to eliminate all values in the array 
            
    if(sequence==temp):
        return True
    else:
        return False
    

array =  [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [5, 1, 22, 22, 25, 6, -1, 8, 10]
x   
result = isValidSubsequence(array, sequence)
print(f"Final output: {result}")