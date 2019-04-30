hours = int(input("Enter hour: "))
minutes = int(input("Enter minute: "))
seconds = int(input("Enter second: "))
am_pm = input("Enter AM or PM: ").lower()
if(hours == 12):
    hours = 0
if(am_pm == "am"):
    minutes = minutes + (hours * 60)
elif(am_pm == "pm"):
    minutes = minutes + ((hours + 12) * 60)
seconds = seconds + (minutes * 60)
print("Seconds since midnight: ", seconds)
