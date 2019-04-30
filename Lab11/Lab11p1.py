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

string = string.upper()
charDict = {}
for c in string:
  if(c.isalpha() == True):
    if(c not in charDict):
      charDict[c] = 1
    elif(c in charDict):
      charDict[c] += 1

print("Dictionary", charDict)

letter = input("Choose a letter: ").upper()
print("Frequency count of that letter: ", charDict[letter])
charDict.pop(letter, None)
print("Dictionary after that letter removed: ", charDict)
charList = sorted(list(charDict.keys()))
print("Letters sorted: ", charList)