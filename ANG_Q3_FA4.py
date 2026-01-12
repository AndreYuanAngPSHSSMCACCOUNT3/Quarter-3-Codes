names = ["Me", "Lia", "Jake"]

steps = [
[4500, 5200, 4800, 5000, 5300],
[4000, 4100, 3900, 4200, 4600],
[6000, 5800, 5900, 6100, 6200]
]


totals = []

for i in range(len(steps)):
total_steps = sum(steps[i])
totals.append(total_steps)
print(names[i], "total steps:", total_steps)

highest_total = max(totals)
lowest_total = min(totals)

highest_person = names[totals.index(highest_total)]

print("Person with highest total steps:", highest_person)
print("Highest total steps:", highest_total)
print("Difference between highest and lowest total:", highest_total - lowest_total)
