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

from waterBill import WaterBill
from electricityBill import ElectricityBill


def main():
    # input name, address and bill_type
    name = input("Enter Name: ")
    address = input("Enter Address: ")

    bill_type = 0
    while(bill_type != 1 and bill_type != 2):
        try:
            bill_type = int(input(
                "Please enter bill_type.\n(1) for Water Bill \n(2) for Electric Bill\n"))
        except ValueError:
            print("Invalid input. bill_type must be a number!")
        if(bill_type != 1 and bill_type != 2):
            print("Error incorrect bill type!")
    if(bill_type == 1):
        waterBill = WaterBill(name, address)
        waterBill.calculate_charge()
        waterBill.display_bill()

    elif(bill_type == 2):
        electricityBill = ElectricityBill(name, address)
        electricityBill.calculate_charge()
        electricityBill.display_bill()


main()
