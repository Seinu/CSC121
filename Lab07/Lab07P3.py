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

    kWh = int(input("Enter kilowatt hours used: "))
    customerType = input(
        "Enter R for residential customer, B for business customer: ").lower()
    bill_calculator(customerType=customerType, kWh=kWh)


def bill_calculator(kWh, customerType):
    if(customerType == "r"):
        if(kWh <= 500):
            price = kWh * 0.12
        elif(kWh > 500):
            kWh -= 500
            price = (500 * 0.12) + (kWh * 0.15)
    elif(customerType == "b"):
        if(kWh <= 800):
            price = kWh * 0.16
        elif(kWh > 800):
            kWh -= 800
            price = (800 * 0.16) + (kWh * 0.20)
    print("Please pay this amount: ", price)


main()
