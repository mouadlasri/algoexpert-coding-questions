# You're hosting an event at a food festival and want to showcase the best
# possible pairing of two dishes from the festival that complement each
# other's flavor profile.
#
# Each dish has a flavor profile represented by an integer. A negative integer
# means a dish is sweet, while a positive integer means a dish is savory. The
# absolute value of that integer represents the intensity of that flavor. For
# example, a flavor profile of -3 is slightly sweet, one of -10 is extremely
# sweet, one of 2 is mildly savory, and one of 8 is significantly savory.
#
# You're given an array of these dishes and a target combined flavor profile.
# Write a function that returns the best possible pairing of two dishes (the
# pairing with a total flavor profile that's closest to the target one). Note
# that this pairing must include one sweet and one savory dish. You're also
# concerned about the dish being too savory, so your pairing should never be
# more savory than the target flavor profile.
#
# All dishes will have a positive or negative flavor profile; there are no
# dishes with a 0 value. For simplicity, you can assume that there will be at
# most one best solution. If there isn't a valid solution, your function
# should return [0, 0]. The returned array should be sorted meaning the sweet dish should always come first
#
# Sample Input #1
# dishes = [-3, -5, 1, 7]
# target = 8 
#
# Sample Output #1
# [-3, 7] // The combined flavor profile of -3 (sweet) and 7 (savory) gives us 4, which is the closest to the target value of 8
#
# Sample Input #2
# dishes = [3, 5, 7, 2, 6, 8, 1]
# target = 10
#
# Sample Output #2
# [0, 0] // there are no sweet dishes
#
# Sample Input #3
# dishes = [2, 5, -4, -7, 12, 100, -25]
# target = -20
#
# Sample Output #3
# [-25, 4] // -25 (sweet) and -4 (savory) have a total flavor profile of -29, which is the closest to the target value of -20


def sweetAndSavory(dishes, target):
     # create sweet and savory dishes list in a sorted way\
    # sort the sweet dishes by their abs value
    # can also do sort(..., reverse=True) instea of sort(...,key=abs)
    sweetDishes = sorted([dish for dish in dishes if dish < 0], key=abs)
    # sweetDishes = sorted([dish for dish in dishes if dish < 0], reverse=True)
    
    savoryDishes = sorted([dish for dish in dishes if dish > 0])

    # starting value (handles empty dishes list too)
    bestPair = [0, 0]
    bestDifference = float('inf')
    sweetIndex, savoryIndex = 0, 0

    while sweetIndex < len(sweetDishes) and savoryIndex < len(savoryDishes):
        # make a dish from both sweet and savory dishes
        currentSum = sweetDishes[sweetIndex] + savoryDishes[savoryIndex]

        
        if currentSum <= target:
            # current difference between target and current sum, we want to minimize this, so we want to get as close to 0 as possible
            currentDifference = target - currentSum 
            if currentDifference < bestDifference: # if current difference is less than the best difference so far, then we have a new best pair
                # save this current pair
                bestDifference = currentDifference
                bestPair = [sweetDishes[sweetIndex], savoryDishes[savoryIndex]]
                
            # we need a higher positive value because the sum is less that the target
            # so, we need to add a dish with a higher savory 
            savoryIndex += 1
        else:
            sweetIndex += 1

    return bestPair


# Example input
dishes = [-3, -5, 1, 7]
target = 8
# Example output
# [-3, 7]

print(sweetAndSavory(dishes, target))