import csv
try:
    with open('../data/messy_data.csv', 'r') as file:
        reader = csv.DictReader(file)
        rows_attempted = 0
        rows_parsed = 0
        clean_data = []
        skipped_rows = []
        for row in reader:
            rows_attempted += 1
            try:
                if None in row:
                    skipped_rows.append(f"Row {rows_attempted}: extra column detected — skipped")
                    continue
                row['amount'] = float(row['amount'])
                rows_parsed += 1
                clean_data.append(row) 
            except ValueError as e:
                skipped_rows.append(f"Row {rows_attempted}: {str(e)}")
                 
            except KeyError as e:
                skipped_rows.append(f"Row {rows_attempted}: {str(e)}")    
        print ('=== CSV Report ===')
        print (f'Rows attempted: {rows_attempted}')
        print (f'Rows parsed: {rows_parsed}')
        print (f'Rows skipped: {len(skipped_rows)}')
        print('\nSkipped rows:')
        for skipped in skipped_rows:
            print(f'  {skipped}') 
             
        print("Clean data: ")        
        for row in clean_data:
            print(f"{row['name']} | {row['category']} | ${row['amount']:.2f}")                       
except FileNotFoundError:
    print('Error: "messy_data.csv" was not found.')