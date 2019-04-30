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

listA = []
for i in range(5, 22, 4):
    listA.append(i)
print(listA)
print("Elements in the first list:")
for i in range(0, len(listA)):
    print(listA[i])

listB = []
for i in range(26, 4, -7):
    listB.append(i)
print(listB)
total = 0
for i in range(0, len(listB)):
    total = total + listB[i]
print(total)
