def bubble_sort (numbers):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(numbers) - 1):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swapped = True
    return numbers    
while True: 
    numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]
    print ('=== Number Cruncher ===')
    print ("1. Find minimum")
    print ("2. Find maximum")
    print ("3. Search for a number")
    print ("4. Sort the list")
    print ("5. Quit")
    print ("Choose an option (1-5):")
    x = int (input('Your option '))
    smallest = (numbers[0])
    largest = (numbers[0])
    if x == 1:
        for number in numbers:
            if number < smallest:
                smallest = number   
        print (f'Minimum number is {smallest}')

    elif x == 2:   
        for number in numbers:                
            if number > largest:
                largest = number
        print (f'Maximum number is {largest}')

    elif x == 3:
        target = int(input("Enter your number "))
        found = False
        index = 0
        for number in numbers:
            if number == target:
               found = True
               break
            index += 1
        if found:
            print(f"Found {target} at index {index}!")
        else:
            print(f"{target} not in the list.")

    if x == 4:            
        print(bubble_sort(numbers))
    elif x == 5:
        print ("Good bye!")   
        break 
    else:
        print("Invalid option. Please choose 1-5.")