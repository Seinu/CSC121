seconds = int(input("Enter Number of seconds since midnight: "))
minutes = int(seconds / 60 ) % 60
hours = int(seconds / (60 * 60))
seconds = seconds % 60
if hours < 12:
    am_pm = " AM"
else:
    am_pm = " PM"
if hours >= 12:
    hours = hours - 12
if(hours == 0):
    hours = 12
print("The time is " + str(hours) + ":" + str(minutes) + ":" + str(seconds) + am_pm)
