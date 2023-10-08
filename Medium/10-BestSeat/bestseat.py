
#   You walk into a theatre you're about to see a show in. The usher within the
#   theatre walks you to your row and mentions you're allowed to sit anywhere
#   within the given row. Naturally you'd like to sit in the seat that gives you
#   the most space. You also would prefer this space to be evenly distributed on
#   either side of you (e.g. if there are three empty seats in a row, you would
#   prefer to sit in the middle of those three seats).
#
#   Given the theatre row represented as an integer array, return
#   the seat index of where you should sit. Ones represent occupied seats and zeroes
#   represent empty seats.
# 
#   You may assume that someone is always sitting in the
#   first and last seat of the row. Whenever there are two equally good seats,
#   you should sit in the seat with the lower index. If there is no seat to sit
#   in, return -1. The given array will always have a length of at least one
#   and contain only ones and zeroes.

# Sample Input:
#   seats = [1, 0, 1, 0, 0, 0, 1]
# Sample Output:
#   4

# Solution 1: O(n) time | O(1) space
def bestSeat(seats):
    bestSeat = -1
    maxSpace = 0

    left = 0 

    while left < len(seats):
        right = left + 1

        # find the range of empty seats starting from left seat until we hit an occupied seat (= 1)
        while right < len(seats) and seats[right] == 0: # find the rightmost empty seat in the range
            right += 1

        availableSpace = right - left - 1 # -1 because we don't want to count the occupied seat  

        if availableSpace > maxSpace:
            bestSeat = (left + right) // 2 # find the middle seat of the empty seats range
            maxSpace = availableSpace

        left = right # move left pointer to the right of the occupied seat we just found (to skip over the seats we just checked)

    return bestSeat

# Input example
seats = [1, 0, 1, 0, 0, 0, 1]
print(bestSeat(seats)) # 4




