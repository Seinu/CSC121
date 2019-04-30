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

import random
listA = []
listB = []
for i in range(0, 5):
    listA.append(random.randint(1, 9))
    listB.append(random.randint(2, 8))
print("First list: ", listA)
print("Second list: ", listB)
print("Larger number in each comparison:")
for i in range(0, 5):
    if(listA[i] > listB[i]):
        print(listA[i])
    elif((listA[i] < listB[i])):
        print(listB[i])
