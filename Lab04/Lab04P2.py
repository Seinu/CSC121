hours = int(input("Enter hour: "))
while(hours < 1 or hours > 12):
    print("Hour must be from 1 to 12.")
    hours = int(input("Enter hour: "))

minutes = int(input("Enter minute: "))
while(minutes < 0 or minutes > 59):
    print("minute must be from 0 to 59.")
    minutes = int(input("Enter minute: "))

seconds = int(input("Enter second: "))
while(seconds < 0 or seconds > 59):
    print("second must be from 0 to 59.")
    seconds = int(input("Enter second: "))

am_pm = input("Enter AM or PM: ").lower()
while(am_pm != "am" and am_pm != "pm"):
    print("Please enter AM or PM")
    am_pm = input("Enter AM or PM: ").lower()

if(hours == 12):
    hours = 0
if(am_pm == "am"):
    minutes = minutes + (hours * 60)
elif(am_pm == "pm"):
    minutes = minutes + ((hours + 12) * 60)
seconds = seconds + (minutes * 60)
print("Seconds since midnight: ", seconds)
