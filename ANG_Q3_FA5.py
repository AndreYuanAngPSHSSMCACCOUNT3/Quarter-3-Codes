names = ["Me", "Lia", "Jake"]

steps = [
[4500, 5200, 4800, 5000, 5300],
[4000, 4100, 3900, 4200, 4600],
[6000, 5800, 5900, 6100, 6200]
]

Code to Calculate Total Steps Per Day and Find the Most Active Day

day_totals = []

for day in range(len(steps[0])):
total = 0
for person in range(len(steps)):
total += steps[person][day]
day_totals.append(total)
print("Day", day + 1, "total steps:", total)

most_active_day = day_totals.index(max(day_totals)) + 1

print("Most active day overall: Day", most_active_day)
