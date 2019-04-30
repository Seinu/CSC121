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
    kWh, customerType = get_user_input()
    price = bill_calculator(kWh, customerType)
    print("Please pay this amount: ", price)


def get_user_input():
    kWh = 0
    while(kWh <= 0):
        kWh = int(input("Enter kilowatt hours used: "))
        if(kWh < 0):
            print("kWh cannot be negative.")
    customerType = ''
    while(customerType != 'R' and customerType != 'B'):
        customerType = input(
            "Enter R for residential customer, B for business customer: ").upper()
        if(customerType != 'R' and customerType != 'B'):
            print("Invalid customer type.")
    return kWh, customerType


def bill_calculator(kWh, customerType):
    if(customerType == "R"):
        if(kWh <= 500):
            price = kWh * 0.12
        elif(kWh > 500):
            kWh -= 500
            price = (500 * 0.12) + (kWh * 0.15)
    elif(customerType == "B"):
        if(kWh <= 800):
            price = kWh * 0.16
        elif(kWh > 800):
            kWh -= 800
            price = (800 * 0.16) + (kWh * 0.20)
    return price


main()
