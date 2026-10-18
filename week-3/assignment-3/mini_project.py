day = input ("What day is today? ") .capitalize()
day_time = input ("What time of the day? ") .lower () 
if (day == "Monday" or day == "Wednesday" or day == "Friday"):
    if day_time == "morning":
        print("Morning Python class — great time to focus!")       
    elif (day_time == "afternoon"):
        print("Time for lunch!")
    elif (day_time == "evening"):   
        print ("Time to rest")
elif (day == "Tuesday" or day == "Thursday"):
    if day_time == "morning":
         print("Go to the gym")    
    elif (day_time == "afternoon"):
         print ("Meet with friend")
    elif (day_time == "evening"): 
         print ("Do yoga class")         
elif (day == "Saturday" or day == "Sunday"):
    if (day_time == "morning"):
        print ("Family time!")
    elif (day_time == "afternoon"):
        print ("Time for your favorite activity!")
    elif (day_time == "evening"):
        print ("Perfect night for a movie or trying a new recipe.")
else: 
    day_time != "morning" and day_time != "afternoon" and day_time !="evening"
    print ("Sorry, I don't recognize that day. Try: Monday, Tuesday, Wednesday...")