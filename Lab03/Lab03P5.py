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

r_b = input("Enter R for residential customer or B for business customer: ").upper()
gallons = float(input("How many gallons of water were used? "))
if(r_b == "R"):
    if(gallons <= 6000):
        total = gallons * 0.005
    elif(gallons > 6000):
        total = ((gallons - 6000) * 0.007) + (6000 * 0.005)
    else:
        print("There was an error")

if(r_b == "B"):
    if(gallons <= 8000):
        total = gallons * 0.006
    elif(gallons > 8000):
        total = ((gallons - 8000) * 0.008) + (8000 * 0.006)
    else:
        print("There was an error")

print("Please pay this amount: $" + str(total))