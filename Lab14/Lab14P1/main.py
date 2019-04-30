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
from deluxeDinnerCombo import DeluxeDinnerCombo


def main():
    # inout meal choice
    choice = 0
    while(choice != 1 and choice != 2):
        try:
            choice = int(input(
                "Please enter choice.\n(1) for Combo\n(2) for Deluxe Combo\n"))
        except ValueError:
            print("Invalid input. Choice must be a number!")
        if(choice != 1 and choice != 2):
            print("Error incorrect choice!")

    if(choice == 1):
        # create DinnerCombo object and call its methods
        dinnerCombo = DinnerCombo()
        dinnerCombo.choose_soup()
        dinnerCombo.choose_main_dish()
        dinnerCombo.displayOrder()

    elif(choice == 2):
        # create DeluxeDinnerCombo object and call its methods
        deluxeDinnerCombo = DeluxeDinnerCombo()
        deluxeDinnerCombo.choose_soup()
        deluxeDinnerCombo.choose_main_dish()
        deluxeDinnerCombo.choose_appetizer()
        deluxeDinnerCombo.displayOrder()


main()
