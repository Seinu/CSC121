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
