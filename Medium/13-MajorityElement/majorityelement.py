
# Write a function that takes in a non-empty, unordered array  of
# positive integers and returns the array's majority element without sorting
# the array and without using more than constant space.

# An array's majority element is an element of the array that appears in over
# half (n/2) of its indices. Note that the most common element of an array (the
# element that appears the most times in the array) isn't necessarily the
# array's majority element; for example, the arrays [3, 2, 2, 1] and [3, 4, 2, 2, 1] both have 2 as their most common element, 
# yet neither array has a majority element, because neither 2 nor any other element appears in over half of the
# respective arrays' indices

# You can assume that there will always be a majority element in the array.

# Sample Input:
# array = [1, 2, 3, 2, 2, 1, 2]
# Sample Output:
# 2 # 2 appears in 4 out of 7 indices (4/7) in the array, and 4 is more than 7/2 = 3, making it the majority element

def majorityElement(array):
    count = 0
    candidate = None # candidate is the majority element in the array 

    for num in array: 
        # if count is 0, then we have a new candidate 
        # because we have seen the current candidate the same amount of times as we have seen other elements 
        if count == 0:  # also handles the initial case where count is 0 and candidate is None
            candidate = num 

        # if the current number is the same as the candidate, then we increment the count 
        # because we have seen the candidate more times than we have seen other elements 
        if num == candidate:
            count += 1 
            
        # if the current number is not the same as the candidate, then we decrement the count
        # because we have seen the candidate the same amount of times as we have seen other elements
        else:
            count -= 1