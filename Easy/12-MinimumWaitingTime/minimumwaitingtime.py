
#   You're given a non-empty array of positive integers representing the amounts
#   of time that specific queries take to execute. Only one query can be executed
#   at a time, but the queries can be executed in any order.
#
#   A query's waiting time is defined as the amount of time that it must wait
#   before its execution starts. In other words, if a query is executed second,
#   then its waiting time is the duration of the first query; if a query is
#   executed third, then its waiting time is the sum of the durations of the
#   first two queries.
#
#   Write a function that returns the minimum amount of total waiting time for
#   all of the queries. For example, if you're given the queries of durations
#   [1, 4, 5], then the total waiting time if the queries were
#   executed in the order of [5, 1, 4] would be
#   (0) + (5) + (5 + 1) = 11. The first query of duration
#   5 would be executed immediately, so its waiting time would be
#   0, the second query of duration 1 would have to wait
#   5 seconds (the duration of the first query) to be executed, and
#   the last query would have to wait the duration of the first two queries before
#   being executed.
#
#   Note: you're allowed to mutate the input array.
#
#   Sample Input
#   queries = [3, 2, 1, 2, 6]
#
#   Sample Output
#   17


def minimumWaitingTime(queries):
    # Write your code here.

    queries.sort()
    # print(queries)
    total = 0
    for index, query in enumerate(queries):
        total += query * (len(queries) - (index + 1))

    return total

# Example input
queries = [3, 2, 1, 2, 6]
print(minimumWaitingTime(queries))
# Expected output: 17

# Intuition: The longer a query takes, the more it contributes to the total
# waiting time. So, we want to execute the longest queries first. This is
# because the longer a query takes, the more time it will have to wait for the
# other queries to finish before it can start.
#
# Solution: Sort the array of queries in place. Then, iterate through the
# sorted array, adding the duration of each query to the total waiting time.
# However, for each query, we must also multiply its duration by the number of
# queries that come after it (i.e., the length of the array minus the index of
# the query in the array minus 1). This is because each of the subsequent
# queries will have to wait the duration of the current query before it can
# start, because there is only one processor. So, the total waiting time for
# each subsequent query is equal to the duration of the current query plus the
# total waiting time of all the queries that come before it.
#
# Time Complexity: O(nlog(n)) time, where n is the length of the input array.
# This is because we have to sort the input array, which takes O(nlog(n)) time
# in the worst case. Then, we have to iterate through the sorted array, which
# takes O(n) time in the worst case.
#
# Space Complexity: O(1) space, because we're not using any additional space
# other than the space we need to store the total waiting time.
#

