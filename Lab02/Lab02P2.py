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

lab01 = int(input("What is your first lab score?"))
lab02 = int(input("What is your second lab score?"))
lab03 = int(input("What is your third lab score?"))
test01 = int(input("What is your first test score?"))
test02 = int(input("What is your second test score?"))
labavg = (lab01 + lab02 + lab03) / 3
print("Your average lab score is " + str(labavg))

testavg = (test01 + test02) / 2
print("Your average test score is " + str(testavg))

grade = (labavg * 0.55) + (testavg * 0.45)
print("Your grade is " + str(grade))
