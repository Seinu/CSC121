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

salary = float(input("Enter first year’s salary: "))
amountRetire = 0
for i in range(10):
    amountRetire = amountRetire + (salary * 0.05)
    print("Year: ", i + 1, "Salary: ", salary)
    print("Retirement Found Total So Far: ", amountRetire, "\n")
    salary = salary + (salary * 0.02)
