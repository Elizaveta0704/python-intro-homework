import os
if os.path.exists("../data/expenses.csv"):
    print("Found it!")
else:
    print("File not found.")
import os
path = os.path.join("..", "data", "expenses.csv")
print(path)
  