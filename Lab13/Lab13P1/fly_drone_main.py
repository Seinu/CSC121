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

from drone import Drone


def main():

    # create Drone object
    drone = Drone()

    # set choice to 5
    choice = 5

    while(choice != 0):

        # input choice
        choice = int(input(
            "Enter 1 for accelerate, 2 for decelerate, 3 for ascend, 4 for descend, 0 for exit: "))

        # if choice is 1, call accelerate method of drone object
        if(choice == 1):
            drone.accelerate()

        # if choice is 2, call decelerate method of drone object
        if(choice == 2):
            drone.decelerate()

        # if choice is 3, call ascend method of drone object
        if(choice == 3):
            drone.ascend()

        # if choice is 4, call descend method of drone object
        if(choice == 4):
            drone.descend()

        if(choice == 0):
            exit()

        # display speed and height of drone object
        print("Speed: ", drone.speed, "Height:  ", drone.height)


main()
