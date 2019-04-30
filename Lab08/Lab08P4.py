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

average = lambda l:sum(l) / len(l)

list1 = [2, 1, 5, 9, 8]
list1_avg = average(list1)
print("list1 average:", format(list1_avg,".2f"))
list2 = [17, 5, 2, 4]
list2_avg = average(list2)
print("list2 average:", format(list2_avg,".2f"))