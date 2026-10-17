day = input ("What day is today? ") .capitalize()
day_time = input ("What time of the day? ") .lower ()
if (day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday"):
    if day_time == "morning":
        print("Morning Python class — great time to focus!")
    elif (day_time == "afternoon"):
        print("Time for lunch!")
    elif (day_time == "evening"):   
        print ("Time to rest")
elif (day == "Saturday" or day == "Sunday"):
    if (day_time == "morning"):
        print ("Family time!")
    elif (day_time == "afternoon"):
        print ("Time for your favorite activity!")
    elif (day_time == "evening"):
        print ("Perfect night for a movie or trying a new recipe.")   
else:
    print ("Sorry, I don't recognize that day. Try: Monday, Tuesday, Wednesday...")