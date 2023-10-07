# intervals = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]

def mergeOverlappingIntervals(intervals):
    sortedIntervals = sorted(intervals, key =lambda x: x[0]) # sort by first element in each interval 
    # create a new list of merged intervals 
    mergedIntervals = []

    # first interval in sorted list of intervals (smallest)
    currentInterval = sortedIntervals[0] # [1, 2]   

    # add the first interval to the merged intervals list, and iterate through the sorted intervals, starting at the second interval, to merge the intervals
    mergedIntervals.append(currentInterval)

    for nextInterval in sortedIntervals:
        currentIntervalStart, currentIntervalEnd = currentInterval
        nextIntervalStart, nextIntervalEnd = nextInterval

        # print(f'currentIntervalStart: {currentIntervalStart}, currentIntervalEnd: {currentIntervalEnd}')
        # print(f'nextIntervalStart: {nextIntervalStart}, nextIntervalEnd: {nextIntervalEnd}')
        # print('\n')
        if currentIntervalEnd >= nextIntervalStart:
            # merge the intervals if they overlap (current interval end is greater than next interval start)
            # set current interval end to the max of the two interval ends  
            # example of such case is [2, 6] and [3, 4] => [2, 6]
            currentInterval[1] = max(currentIntervalEnd, nextIntervalEnd) 

        else:
            currentInterval = nextInterval

            # add the current interval to the merged intervals list if they don't overlap 
            mergedIntervals.append(currentInterval) 

    return mergedIntervals

# Time Complexity: O(nlogn) - sorting the intervals takes O(nlogn) time, and iterating through the intervals takes O(n) time
# Space Complexity: O(n) - creating a new list of merged intervals takes O(n) space

# Input Example:
intervals = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]
# Output Example:
# [[1, 2], [3, 8], [9, 10]]

print(mergeOverlappingIntervals(intervals))
