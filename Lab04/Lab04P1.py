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

boolChkPatient = "y"
while(boolChkPatient != "n"):
    FPG = int(input("Enter fasting plasma glucose level: "))
    if(FPG > 125):
        print("This patient has diabetes\n")
    elif(FPG <= 125 and FPG > 100):
        print("This patient has pre-diabetes\n")
    elif(FPG <= 100):
        print("This patient has healthy fpg level\n")
    boolChkPatient = input(
        "Checking diabetes for another patient? [y/n] ").lower()
