numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

def find_min(numbers):
   smallest = (numbers[0])
   for number in numbers:
        if number < smallest:
           smallest = number  

   return smallest

def find_max(numbers):
    largest = (numbers[0])
    for number in numbers:
        if number > largest:
            largest = number
    return largest      

def search(numbers, target):
    index = 0
    for number in numbers: 
        if number == target:
           return index
        index += 1
   
    return -1 

def bubble_sort (numbers):
    sorted_numbers = numbers.copy()
    for i in range(len(sorted_numbers) - 1):
        for p in range(len(sorted_numbers) - 1 - i):
            if sorted_numbers[p] > sorted_numbers[p + 1]:
                sorted_numbers[p], sorted_numbers[p + 1] = sorted_numbers[p + 1], sorted_numbers[p]
                
    return sorted_numbers    

def show_menu():
    print ('1. Find minimum')
    print('2. Find maximum')
    print('3. Search for a number')
    print('4. Sort numbers')
    print('5. Exit')
    option = (input('Enter your option: '))
    return option

def main ():
    while True:
        option = show_menu()
        if option == '1':
            print(find_min(numbers))
        elif option == '2':
            print(find_max(numbers)) 
        elif option == '3':
            print (numbers)
            target = int(input('Enter your number: '))
            index = search(numbers, target)
            if index != -1:
                print (f'found at index {index}')
            else:
                print('Not found')
        elif option == '4':
            sorted_numbers = bubble_sort (numbers)
            print (sorted_numbers)  
        elif option == '5':
            print ('Good bye!')
            break     
        else:
            print('Invalid option. Try again.')     
main()                   