import os
import csv
from datetime import datetime
if os.path.exists("../data/expenses.csv"):
     print("expenses.csv found.")
else:
    print("expenses.csv doesn't exis.")
    exit()
with open('../data/expenses.csv', 'r') as file:
    reader = csv.DictReader(file)    
    foods = []
    total = 0
    for row in reader:
        row['amount'] = float(row['amount'])
        if row ['category'] == 'Food':
            foods.append(row)
            total += row['amount']
                
with open('food_report.txt','w') as file:
    now = datetime.now()
    file.write(f'Food Expense Report - generated {now.strftime("%B %d, %Y")}\n')
    for food in foods:
        file.write(f'{food['date']}: ${food['amount']}\n')
    file.write(f'Total: ${total:.2f}\n')   
