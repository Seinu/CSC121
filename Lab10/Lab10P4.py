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

string = input("Enter a string: ")
print(string)
string = string.upper()
charList = [[],[]]
for c in string:
  if(c.isalpha() == True):
    if(c not in charList[0]):
      charList[0].append(c)
      charList[1].append(1)
    elif(c in charList[0]):
      tmp = charList[0].index(c)
      charList[1][tmp] += 1

for i in range(0, len(charList[0])):
  print(charList[0][i], charList[1][i])
