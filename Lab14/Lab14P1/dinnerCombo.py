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

class DinnerCombo:

    def __init__(self):
        # create self._soup, self._main_dish, initialize then to empty strings
        self._soup = ""
        self._main_dish = ""
        # create self._total, initialize it to 0
        self._total = 0.0

    def choose_soup(self):
        # input choice, store soup name in self._soup and add soup price to self._total
        choice = 0
        while(choice != 1 and choice != 2):
            try:
                choice = int(input(
                    "Please enter soup choice.\n(1) for Egg Drop Soup $1.25\n(2) for Wanton Soup $1.50\n"))
            except ValueError:
                print("Invalid input. Choice must be a number!")
            if(choice != 1 and choice != 2):
                print("Error incorrect choice!")
        if(choice == 1):
            self._soup = "Egg Drop Soup"
            self._total = self._total + 1.25
        elif(choice == 2):
            self._soup = "Wanton Soup"
            self._total = self._total + 1.5

    def choose_main_dish(self):
        # input choice, store main dish name in self._main_dish and add main dish price to self._total
        choice = 0
        while(choice != 1 and choice != 2 and choice != 3):
            try:
                choice = int(input(
                    "Please enter main dish choice.\n(1) for Sweet and Sour Pork $7\n(2) for Sesame Chicken $8\n(3) for Shrimp Fried Rice $9\n"))
            except ValueError:
                print("Invalid input. Choice must be a number!")
            if(choice != 1 and choice != 2 and choice != 3):
                print("Error incorrect choice!")
        if(choice == 1):
            self._main_dish = "Sweet and Sour Pork"
            self._total = self._total + 7.0
        elif(choice == 2):
            self._main_dish = "Sesame Chicken"
            self._total = self._total + 8.0
        elif(choice == 3):
            self._main_dish = "Shrimp Fried Rice"
            self._total = self._total + 9.0

    def displayOrder(self):
        # display self._soup, self._main_dish and self._total
        print("You ordered the dinner combo with ", self._main_dish,
              "for your main dish and ", self._soup, "for your soup.")
        print("Your total is: ", self._total)
