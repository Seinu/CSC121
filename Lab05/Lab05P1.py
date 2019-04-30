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

numL = []
boolCont = 'y'
avg = 0.0
while(boolCont == 'y'):
    numL.append(int(input("Enter an integer from 1 to 10: ")))
    boolCont = input("Enter another integer? [y/n] ").lower()

for i in range(0, len(numL)):
    avg += numL[i]

avg = avg / len(numL)

print("Number list: ", numL)
print("Average: ", avg)

if(avg > 7):
    for i in range(0, len(numL)):
        numL[i] = numL[i] - 1
print("Modified Number list: ", numL)
