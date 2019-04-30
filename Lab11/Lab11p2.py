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

from random import randint
set1 = set()
set2 = set()
for i in range(0, 5):
    set1.add(randint(1, 10))
    set2.add(randint(1, 10))

print("set1: ", set1)
print("set2: ", set2)
print("Union of set1 and set2: ", set1.union(set2))
print("Odd numbers in union of set1 and set2: ", {
      x for x in set1.union(set2) if x % 2 == 1})
print("Intersection of set1 and set2: ", set1 & set2)
print("Symmetric difference of set1 and set2: ", set1 ^ set2)
