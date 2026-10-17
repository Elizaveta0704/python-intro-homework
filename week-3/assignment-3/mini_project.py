day = input ("What day is today? ") .capitalize()
day_time = input ("What time of the day? ") .lower ()
if (day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday") and day_time == "morning":
    print("Morning Python class — great time to focus!")
elif (day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday"or day == "Friday") and day_time == "afternoon":
   print("Time for lunch!")
elif (day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday") and day_time == "evening":   
    print ("Time to rest")
elif day == "Saturday" and day_time == "morning" or day == "Sunday" and day_time == "morning":
    print ("Family time!")
elif day == "Saturday" and day_time == "afternoon" or day == "Sunday" and day_time == "afternoon":
    print ("Time for your favorite activity!")
elif day == "Saturday" and day_time == "evening" or day == "Sunday" and day_time == "evening":
    print ("Perfect night for a movie or trying a new recipe.")   
else:
    print ("Sorry, I don't recognize that day. Try: Monday, Tuesday, Wednesday...")