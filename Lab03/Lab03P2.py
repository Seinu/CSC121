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
