# Copyright (C) 2019 Seinu
#
# This file is part of CSC121.
# NOT FOR COLLEGE REUSE
#
# CSC121 is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# CSC121 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with CSC121.  If not, see <http://www.gnu.org/licenses/>.
#
# NOT FOR COLLEGE REUSE

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