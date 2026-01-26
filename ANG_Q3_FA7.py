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
