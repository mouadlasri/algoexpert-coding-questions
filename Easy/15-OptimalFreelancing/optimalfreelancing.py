
# You recently started freelance software development and have been offered
# a variety of job opportunities. Each job has a deadline, meaning there is no
# value in completing the work after the deadline. Additionally, each job
# has an associated payment representing the profit for completing that job.
# Given this information, write a function that returns the maximum profit that
# can be obtained in a 7-day period.

# Each job will take 1 full day to complete, and the deadline will be given
# as the number of days left to complete the job. For example, if a job has a
# deadline of 1, then it can only be completed if it is the first job worked
# on. If a job has a deadline of 2, then it could be started on the first or
# second day.

# Note: There is no requirement to complete all of the jobs. Only one job can
# be worked on at a time, meaning that in some scenarios it will be impossible
# to complete them all.

# Sample input
# jobs = [
#     {"deadline": 1, "payment": 1},
#     {"deadline": 2, "payment": 1},
#     {"deadline": 2, "payment": 2}
# ]

# Sample output
# 3 // Job 0 would be completed first, followed by job 2. Job 1 is not completed.

def optimalFreelancing(jobs):
    LENGTH_OF_WEEK = 7
    profit = 0
    jobs.sort(key= lambda job: job['payment'], reverse=True)

    # timeline that represents the days of the week
    # any value of False means we still have a time slot to do a job on that day
    # any value of True means we found a job to do on that day, and accounted for its profit
    timeline = [False] * LENGTH_OF_WEEK 

    for job in jobs:
        # latest possible time (day) in the timeline that we can put our job in
        maxTime = min(job['deadline'], LENGTH_OF_WEEK)
        for time in reversed(range(maxTime)):
            if(timeline[time] == False):
                timeline[time] = True
                profit = profit + job['payment']
                break

    return profit

# explanation of the function optimalFreelancing
# 1. sort the jobs by payment in descending order
# 2. create a timeline that represents the days of the week
# 3. iterate through the jobs
# 4. for each job, find the latest possible time (day) in the timeline that we can put our job in
# 5. iterate backwards through the timeline, starting at the latest possible time
# 6. if the timeline at the current time is False, then we can put our job in that time slot
# 7. set the timeline at the current time to True, to indicate that we found a job to do on that day
# 8. add the job's payment to the profit
# 9. break out of the loop, since we found a job to do on that day
# 10. return the profit


# Example input
jobs = [
    {"deadline": 1, "payment": 1},
    {"deadline": 2, "payment": 1},
    {"deadline": 2, "payment": 2}
]
print(optimalFreelancing(jobs))
# Expected output: 14


