# Create an empty dictionary named student
student = {}

# Use input() to collect the necessary details
# We assign the inputs to variables first
name_input = input("Enter your name: ")
age_input = input("Enter your age: ")
subject_input = input("Enter your favorite subject: ")

# Store the data into the dictionary with the specific keys
student["name"] = name_input
student["age"] = age_input
student["subject"] = subject_input

# Print the student's information in a clear format
print("\nStudent Record:")
print("Name:", student["name"])
print("Age:", student["age"])
print("Favorite Subject:", student["subject"])
