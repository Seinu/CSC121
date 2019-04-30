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

height = float(input("Enter initial height: "))
bounceIndex = float(input("Enter bounciness index: "))
numBounceCount = int(
    input("Enter number of times the ball is allowed to bounce: "))
for i in range(numBounceCount):
    height = height * bounceIndex
    print("Number of bounces: ", i + 1, " Height: ", height)
