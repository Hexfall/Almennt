mon, day = input("Month: "), input("Day: ")
dags = mon.capitalize() + " " + day
if (dags == "January 1"):
    print("New year's day")
elif (dags == "June 17"):
    print("National holiday")
elif (dags == "December 25"):
    print("Christmas day")
else:
    print("Not a holiday")