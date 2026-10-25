# and the name that goes with it. Do not use Python's built-in max() on the list directly.
# Calculate the class average — accumulate the total score in a loop, then divide.
# List all unique subjects — use a set to collect subjects as you loop, then print them.
# List high scorers — use a loop and .append() to get the names of all students who scored above 75.
students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
]
top_scorer = []
for student in students:
     if student["score"] >= 95:
        top_scorer.append(student["name"]), 
print(top_scorer)
total = 0
for student in students:
    total += student["score"]
average = total / len(students)
print(f"Class average: {average}")
high_scorers = []
for student in students:
     if student["score"] >= 75:
        high_scorers.append(student["name"]), 
print(high_scorers)