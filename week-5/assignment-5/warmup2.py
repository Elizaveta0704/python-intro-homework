number = input ("Enter a positive integer ")
while number.isdigit() == False or int(number) < 1:
    print ("That's not a positive integer. Try again.")
    number = input ('Enter a positive integer')   
print (f"Got it: {number}")