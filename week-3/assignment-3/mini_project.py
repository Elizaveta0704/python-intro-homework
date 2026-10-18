day = input ("What day is today? ") .capitalize()
day_time = input ("What time of the day? ") .lower () 
if (day != "Monday" and day != "Tuesday" and day != "Wednesday" and day != "Thursday" and day != "Friday" and day != "Saturday" and day != "Sunday"):
    print("Sorry, I don't recognize that day. Try: Monday, Tuesday, Wednesday...")
elif (day_time != "morning" and day_time != "afternoon" and day_time != "evening"):
    print("Sorry, I don't recognize that part of the day")
elif (day == "Monday" or day == "Wednesday" or day == "Friday"):
    if day_time == "morning":
        print("Morning Python class — great time to focus!")       
    elif (day_time == "afternoon"):
        print("Time for lunch!")
    else:  
        print ("Time to rest")   
elif (day == "Tuesday" or day == "Thursday"):
    if day_time == "morning":
         print("Go to the gym")    
    elif (day_time == "afternoon"):
         print ("Meet with friend")
    else:
         print ("Do yoga class")   
             
elif (day == "Saturday" or day == "Sunday"):
    if (day_time == "morning"):
        print ("Family time!")
    elif (day_time == "afternoon"):
        print ("Time for your favorite activity!")
    else:
        print ("Perfect night for a movie or trying a new recipe.")    
