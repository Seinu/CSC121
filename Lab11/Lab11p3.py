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

try:
    hotdogs = int(input("How many hotdogs do you want? "))
except ValueError:
    print("Invalid input. Number of hotdogs set to 0.")
    hotdogs = 0


try:
    chips = int(input("How many chips do you want? "))
except ValueError:
    print("Invalid input. Number of chips set to 0.")
    chips = 0

try:
    sodas = int(input("How many sodas do you want? "))
except ValueError:
    print("Invalid input. Number of sodas set to 0.")
    sodas = 0

print("Your total is $" +
      str(format((hotdogs * 2.50)+(chips * 1.50)+(sodas * 1.25), '.2f')))
