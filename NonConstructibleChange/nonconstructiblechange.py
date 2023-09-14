
#   Given an array of positive integers representing the values of coins in your
#   possession, write a function that returns the minimum amount of change (the
#   minimum sum of money) that you cannot  create. The given coins can have
#   any positive integer value and aren't necessarily unique (i.e., you can have
#   multiple coins of the same value).

# sample input: coins = [5, 7, 1, 1, 2, 3, 22]
# sample output: 20

def nonConstructibleChange(coins):
    # Write your code here.
    change = 0

    coins.sort() # soirt the list in place
    
    for coin in coins:
        if (coin > (change + 1)):
            return (change + 1) # we can't return a change of (change + 1) value
        else:
            change += coin # we can make up changes until the new coin we have
    
    return change + 1


# Official Solution (not intuitive at all):
# if value in array > change + 1, then we can't make up the change of (change + 1)
# if value in array <= change + 1, then we can make up the change of (change + value)