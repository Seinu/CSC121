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

# CONSTANTS
p = 4
n = 6

# Create Empty List Inside of a List
powMatrix = [[]]

# Counter for list index
counter = 0

# For Loop for calculating the numbers to get the power of
# Uses the CONSTANT n for the number
# n + 1 is required for proper loop through range

for i in range(2, n+1):
    # Second For Loop for calculatating powers of the numbers
    # uses CONSTANT p for power
    # p + 1 is required for proper loop through range
    for x in range(1, p+1):
        # appends i to the power of x
        # where i is the number to get the power of
        # and x is the power
        # uses variable counter for proper indexing
        powMatrix[counter].append(i ** x)
    # increase index counter for proper append
    counter += 1
    # if i is equal to the last number to get power of
    # Then break out of loop
    if(i == n):
        break
    # append another empty list to the list powMatrix

    # TODO consider removing break from the above if
    # and change if to i <= n and just directly append
    # an Empty List to powMatrix
    powMatrix.append([])

# Display list at index 0 of powMatrix which is power of 2
# Display list at index 0 of powMatrix which is power of 3
# Display full powers Matrix powMatrix
print("Powers of 2: ", powMatrix[0])
print("Powers of 3 ", powMatrix[1])
print("Matrix: ", powMatrix)
