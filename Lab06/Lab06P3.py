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
NUM_SCORES = 4

# Display text
print("Please enter Jean's scores one by one.")
# Create Empty List jeanList
jeanList = []
# For Loop i in range 0 to CONSTANT NUM_SCORES
for i in range(0, NUM_SCORES):
    # prompt for a score convert to float and append
    # to list jeanList
    jeanList.append(float(input("Enter a score: ")))

# Display list jeanList containing Jean's Scores
print("Jean's scores: ", jeanList, "\n")

# Display text
print("Please enter Kayla's scores one by one.")
# Create Empty List kaylaList
kaylaList = []
# For Loop i in range 0 to CONSTANT NUM_SCORES
for i in range(0, NUM_SCORES):
    # prompt for a score convert to float and append
    # to list kaylaList
    kaylaList.append(float(input("Enter a score: ")))

# Display list kaylaList containing Kayla's Scores
print("Kayla's scores: ", kaylaList, "\n")

# Display text
print("Please enter Connie's scores one by one.")
# Create Empty List connieList
connieList = []
# For Loop i in range 0 to CONSTANT NUM_SCORES
for i in range(0, NUM_SCORES):
    # prompt for a score convert to float and append
    # to list connieList
    connieList.append(float(input("Enter a score: ")))

# Display list connieList containing Connie's Scores
print("Connie's scores: ", connieList, "\n")

# Create List listOfScoreLists containing the lists
# jeanList, kaylaList, connieList
listOfScoreLists = [jeanList, kaylaList, connieList]
# print matrix listOfScoreLists
print("All scores: ", listOfScoreLists)

# For Loop Inside a For Loop
# loops through entire matrix listOfScoreLists
# increases each score by 1
for i in range(0, len(listOfScoreLists)):
    for x in range(0, len(listOfScoreLists[i])):
        listOfScoreLists[i][x] += 1

# Display Matrix listOfScoreLists with updated scores
print("All scores after extra point: ", listOfScoreLists)

# sort each list of Scores in Matrix listOfScoreLists
for i in range(0, len(listOfScoreLists)):
    listOfScoreLists[i].sort()

# Display Sorted Matrix
print("All scores after sorting: ", listOfScoreLists)
