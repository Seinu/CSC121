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

from utilityBill import UtilityBill


class WaterBill(UtilityBill):

    def __init__(self, name, address):
        # call super().__init__, pass name and address as arguments
        super().__init__(name, address)

        # initialize self._gallons_used to 0
        self._gallons_used = 0

    def calculate_charge(self):
        # input self._gallons_used
        try:
            self._gallons_used = int(
                input("Please input number of gallons used: "))
        except ValueError:
            print("Invalid input. Choice must be a number!")

        # calculate self._charge
        if(self._gallons_used <= 6000):
            self._charge = self._gallons_used * 0.005
        elif(self._gallons_used > 6000):
            tmp = self._gallons_used - 6000
            self._charge = (6000 * 0.005) + (tmp * 0.007)

    def display_bill(self):
        # display all instance variables
        print("Name: ", self._name, "\nAddress: ", self._address, "\nGallons used: ",
              self._gallons_used, "\nPlease pay this amount: ", self._charge)
