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

from dinnerCombo import DinnerCombo


class DeluxeDinnerCombo(DinnerCombo):

    def __init__(self):
        # call super().__init__()
        base = super().__init__()
        # create self._appetizer and initialize it to empty string
        self._appetizer = ""

    def choose_appetizer(self):
        # input choice, store appetizer name in self._apprtizer and add appetizer price to self._total
        choice = 0
        while(choice != 1 and choice != 2):
            try:
                choice = int(input(
                    "Please enter appetizer choice.\n(1) for Spring Roll $1.25\n(2) for Chicken Wing $1.50\n"))
            except ValueError:
                print("Invalid input. Choice must be a number!")
            if(choice != 1 and choice != 2):
                print("Error incorrect choice!")
        if(choice == 1):
            self._appetizer = "Spring Roll"
            self._total = self._total + 1.25
        elif(choice == 2):
            self._appetizer = "Chicken Wing"
            self._total = self._total + 1.5

    def displayOrder(self):
        # display self._appetizer, self._soup, self._main_dish and self._total
        print("You ordered the dinner combo with ", self._main_dish,
              "for your main dish, ", self._soup, "for your soup, and ", self._appetizer, "for your appetizer.")
        print("Your total is: ", self._total)
