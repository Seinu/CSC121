time = input("Enter time [hh:mm:ss]: ")
if(time.count(":") != 2 ):
  print("Error: time must have exactly two colons")
  exit()
timeList = time.split(":")


for i in range(0, len(timeList)):
  if(timeList[i].isdigit() == False):
    print("Error: time must use a 2 digit number")
    exit()
  if(len(timeList[i]) != 2):
    print("Error: time must use a 2 digit number")
    exit()

hours = int(timeList[0])
minutes = int(timeList[1])
seconds = int(timeList[2])

if(hours < 0 or hours > 23):
    print("Hour must be a 2 digit number from 1 to 12.")
    exit()
if(minutes < 0 or minutes > 59):
    print("minute must be a 2 digit number from 0 to 59.")
    exit()
if(seconds < 0 or seconds > 59):
    print("second must be a 2 digit number from 0 to 59.")
    exit()
time = timeList[0] + timeList[1] + timeList[2]
print("Time with colons removed: ", time)