while True: 
    try: 
        number = float(input('Enter a number: '))
    except ValueError:
        print("That's not a valid number. Try again.")
        continue
    print(f"You entered: {number}")
    break
        
