students = ["Jazmine", "Carlos", "Amir", "Priya"]
target = input ("Enter your name")
found = False
index = 0
for student in students:
    if student == target:
        found = True
        break
    index +=1
if found:
    print(f"Found {target} at index {index}!")
else:
    print(f"{target} not in the list.")