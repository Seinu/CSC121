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


class ElectricityBill(UtilityBill):

    def __init__(self, name, address):
        # call super().__init__, pass name and address as arguments
        super().__init__(name, address)

        # initialize self._kwh_used to 0
        self._kwh_used = 0

    def calculate_charge(self):
        # input self._kwh_used
        try:
            self._kwh_used = int(
                input("Please input number of kwh used: "))
        except ValueError:
            print("Invalid input. Choice must be a number!")

        # calculate self._charge
        if(self._kwh_used <= 500):
            self._charge = self._kwh_used * 0.12
        elif(self._kwh_used > 500):
            tmp = self._kwh_used - 500
            self._charge = (500 * 0.12) + (tmp * 0.15)

    def display_bill(self):
        # display all instance variables
        print("Name: ", self._name, "\nAddress: ", self._address, "\nKwh used: ",
              self._kwh_used, "\nPlease pay this amount: ", self._charge)
