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

s_e = input("Enter S for standard shipping, E for express: ").upper()
weight = float(input("Enter weight (lbs): "))
if(s_e == "S"):
    if(weight <= 4.0):
        rate = 1.05
    elif(weight > 4.0 and weight <= 8.0):
        rate = 0.95
    elif(weight > 8.0 and weight <= 15.0):
        rate = 0.85
    else:
        rate = 0.80

if(s_e == "E"):
    if(weight <= 2.0):
        rate = 3.25
    elif(weight > 2.0 and weight <= 5.0):
        rate = 2.95
    elif(weight > 5.0 and weight <= 10.0):
        rate = 2.75
    else:
        rate = 2.55

shipCharge = weight * rate
print("Shipping charge:  " + str(shipCharge))