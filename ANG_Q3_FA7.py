--- CODE SECTION ---

Dataset: Student grades (Math, Science, English, History)
grades = [ [85, 90, 88, 92], [78, 82, 80, 85], [92, 95, 93, 98] ]

print("STUDENT PERFORMANCE SUMMARY")

highest_grade = 0

for i in range(len(grades)): current_student_grades = grades[i]

# Calculate summary statistics
total = sum(current_student_grades)
average = total / len(current_student_grades)

# Check for max value in the whole set
for score in current_student_grades:
    if score > highest_grade:
        highest_grade = score
        
# Display results
print("Student", i + 1, "Grades:", current_student_grades)
print("Total Score:", total)
print("Average Score:", average)
print("--------------------")
print("Highest grade in the entire class:", highest_grade)

--- SAMPLE OUTPUT ---

STUDENT PERFORMANCE SUMMARY Student 1 Grades: [85, 90, 88, 92] Total Score: 355 Average Score: 88.75
Student 2 Grades: [78, 82, 80, 85] Total Score: 325 Average Score: 81.25
Student 3 Grades: [92, 95, 93, 98] Total Score: 378 Average Score: 94.5
Highest grade in the entire class: 98

--- WRITTEN EXPLANATION ---

Using a 2D array allowed me to keep all the grades for a specific student in one single row, which made the data much easier to read at a glance. It helped me analyze the results faster because I could use a loop to perform the same calculations on every student without writing unique code for each person. The easiest part was calculating the totals using the sum function, while the most difficult part was setting up the nested loop logic to find the highest score across the entire table.
