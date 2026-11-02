# Job Sequencing using Greedy Method

n = int(input("Enter number of jobs: "))
jobs = []

# Step 1: Accept job details
for i in range(n):
    job = input("Enter job ID: ")
    deadline = int(input("Enter deadline: "))
    profit = int(input("Enter profit: "))
    jobs.append((job, deadline, profit))

# Step 2: Sort jobs by profit
jobs.sort(key=lambda x: x[2], reverse=True)

# Step 3: Create time slots
slots = [None] * max(j[1] for j in jobs)
total_profit = 0

# Step 4: Schedule jobs
for job, deadline, profit in jobs:
    for i in range(min(deadline, len(slots)) - 1, -1, -1):#range(start, stop, step)
        if slots[i] is None:
            slots[i] = job
            total_profit += profit
            break

# Step 5: Display result
print("Scheduled Jobs:", [j for j in slots if j])
print("Maximum Profit:", total_profit)

# Sample Input:
# Number of jobs: 4
# Job ID: J1, Deadline: 2, Profit: 100
# Job ID: J2, Deadline: 1, Profit: 50
# Job ID: J3, Deadline: 2, Profit: 20
# Job ID: J4, Deadline: 3, Profit: 10
#The simple job sequencing implementation has a worst-case complexity of O(n²) because for each job we may search through multiple slots.
#  Sorting itself takes O(n log n).