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

import currency

def main():
  print("Converting US Dollar to a foreign currency.")
  curr,dollar = 0,-1
  while(curr != 1 and curr != 2 and curr != 3):
    curr =  int(input("Enter 1 for Euro, 2 for Japanese Yen, 3 for Mexican Peso: "))
    if(curr != 1 and curr != 2 and curr != 3):
      print("Error: Invalid Choice")

  while(dollar < 0):
    dollar = int(input("Enter US Dollar: "))
    if(dollar < 0):
      print("Error: US Dollar cannot be negative.")
      

  if(curr == 1):
    print("It is converted to ", currency.to_euro(dollar), " Euro")
  if(curr == 2):
    print("It is converted to ", currency.to_yen(dollar), " Yen")
  if(curr == 3):
    print("It is converted to ", currency.to_peso(dollar), " peso")

main()