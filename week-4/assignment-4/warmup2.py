# Create a hardcoded dictionary representing a student with these keys: name, grade, and subjects (a list of subject strings).
#  Then: Print each key-value pair using .items() in a for loop
# Add a new key "graduated" with the value False
# Print the updated dictionary
student = {
    'name': "Kate", 
    'grade': 5, 
    'subjects': ['Math', 'Science', 'Phisics', 'Art']
}
for item in student:
    print(list(student.items())) 