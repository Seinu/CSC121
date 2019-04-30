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
        # initialize self.speed to 0
        self.speed = 0
        # initialize self.height to 0
        self.height = 0

    def accelerate(self):
        # increase self.speed by 10
        self.speed += 10

    def decelerate(self):
        # decrease self.speed by 10
        self.speed -= 10
        # if self.speed is less than 0, change it to 0
        if(self.speed < 0):
            self.speed = 0

    def ascend(self):
        # increase self.height by 10
        self.height += 10

    def descend(self):
        # decrease self.height by 10
        self.height -= 10
        # if self.height is less than 0, change it to 0
        if(self.height < 0):
            self.height = 0
