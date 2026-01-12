Activity 2: Summarizing Your Dataset with Arrays (ILA)

Dataset Used
This activity uses the same 2D array from Activity 1, which represents the weekly test scores of 5 students in 3 subjects: Math, Science, and English.

Sample 2D Array (Python Syntax)

scores = [
[85, 90, 88],
[78, 82, 80],
[92, 95, 94],
[75, 75, 73],
[88, 85, 90]
]

Code to Print, Calculate Totals, Averages, and Maximum Value

for i in range(len(scores)):
print("Student", i + 1, "scores:", scores[i])
total = sum(scores[i])
average = total / len(scores[i])
print("Total:", total)
print("Average:", average)

max_score = max(max(row) for row in scores)
print("Highest score in the dataset:", max_score)

Explanation (3–4 sentences)
Using a 2D array made it easier to organize and analyze the test scores because each student’s data was stored in a single row. This allowed me to use loops to calculate totals and averages without repeating code. Finding the total and average for each student was easy because the values were already grouped together. The only challenging part was remembering how to loop through each row correctly.
