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

#import random
import random

# CONSTANTS
NUM_NUMBERS = 10
RAND_MIN = 1
RAND_MAX = 15

# Create Empty List listA
listA = []

# For Loop where i is index in range of 0 to
# CONSTANT NUM_NUMBERS
for i in range(NUM_NUMBERS):
    # Append a random Integer to listA
    listA.append(random.randint(RAND_MIN, RAND_MAX))

# convert list listA to tuple tupleA
tupleA = tuple(listA)
# Display tupleA
print("Tuple of 10 random numbers: ", tupleA)

# Convert index 0 to 3 of listA to a tuple
# and assign to tupleB
tupleB = tuple(listA[0:3])

# Convert index of CONSTANT NUM_NUMBERS -3 to
# the ending index of CONSTANT NUM_NUMBES
# to a tuple and assign to tupleC
tupleC = tuple(listA[NUM_NUMBERS-3:NUM_NUMBERS])
# Display tupleB and tupleC
print("Tuple of first 3 numbers: ", tupleB,
      "\nTuple of last 3 numbers: ", tupleC)

# convert and concatonate tupleB and tupleC
# to a list and assign to concatList
concatList = list(tupleB) + list(tupleC)
# convert concatList to tuple
# and assign to concatTuple
concatTuple = tuple(concatList)
# sort the list concatLIst and convert to tuple
# Assign it to sortedTuple
sortedTuple = tuple(sorted(concatList))
# Display the concantonated tuple concatTuple
# Display the sorted tuple sortedTuple
print("Two tuples concatenated: ", concatTuple,
      "\nTwo tuples concatcatenated and sorted: ", sortedTuple)
