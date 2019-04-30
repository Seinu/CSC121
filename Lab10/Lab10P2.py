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

def main():
    gallons, customerType, accNum = read_data()
    #print(accNum, "\n", customerType, "\n", gallons)
    for i in range(0, len(accNum)):
      price = bill_calculator(int(gallons[i]), customerType[i])
      print("Account Number: ", accNum[i], " Water charge: {:0.2f}".format(price))
    #price = bill_calculator(gallons, customerType)
    #print("Please pay this amount: ", price)


def read_data():
    accNum = []
    gallons = []
    customerType = []
    dataFile = open("water.txt", "r")
    textData = dataFile.readlines()
    
    for i in range(0, len(textData)):
      tmp = textData[i].split()
      accNum.append(tmp[0])
      customerType.append(tmp[1])
      gallons.append(tmp[2])
    return gallons, customerType, accNum


def bill_calculator(gallons, customerType):
    if(customerType == "R"):
        if(gallons <= 6000):
            price = gallons * 0.005
        elif(gallons > 6000):
            gallons -= 6000
            price = (6000 * 0.005) + (gallons * 0.007)
    elif(customerType == "B"):
        if(gallons <= 8000):
            price = gallons * 0.006
        elif(gallons > 8000):
            gallons -= 8000
            price = (8000 * 0.006) + (gallons * 0.008)
    return price


main()
