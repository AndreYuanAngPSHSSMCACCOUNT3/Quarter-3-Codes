Activity 1: Planning a Mini-Dataset Project

Real-World Scenario
I chose the weekly test scores of 5 students in 3 subjects: Math, Science, and English. This is a common real-life school situation where data is naturally arranged in rows and columns.

2D Array Structure
Each row represents one student.
Each column represents one subject.
Column 0 is Math, Column 1 is Science, and Column 2 is English.

Sample 2D Array (Python Syntax)

scores = [
[85, 90, 88],
[78, 82, 80],
[92, 95, 94],
[70, 75, 73],
[88, 85, 90]
]

Sample Code to Access, Update, and Summarize Data

print(scores[2][1])
scores[3][0] = 75
average_math = sum(row[0] for row in scores) / len(scores)
print(average_math)

Reflection
I chose this dataset because test scores are a realistic and relatable example of data used in school. A 2D array helps organize the data clearly by separating students and subjects into rows and columns. This makes it easy to access specific values, update scores, and compute summaries like averages. Using a 2D array also helps me understand how real-world data can be modeled in programming.
