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

class Drone:

    def __init__(self):
        # initialize self.__speed to 0
        self.__speed = 0
        # initialize self.__height to 0
        self.__height = 0

    def accelerate(self):
        # increase self.__speed by 10
        self.__speed += 10

    def decelerate(self):
        # decrease self.__speed by 10
        self.__speed -= 10
        # if self.s__peed is less than 0, change it to 0
        if(self.__speed < 0):
            self.__speed = 0

    def ascend(self):
        # increase self.__height by 10
        self.__height += 10

    def descend(self):
        # decrease self.__height by 10
        self.__height -= 10
        # if self.__height is less than 0, change it to 0
        if(self.__height < 0):
            self.__height = 0

    def __str__(self):
        return "Speed: " + str(self.__speed) + "  Height: " + str(self.__height)
