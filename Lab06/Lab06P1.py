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
NUM_SCORES = 5
MIN_SCORE = 60
ADD_SCORE = 10

# Create an Empty List listScores
listScores = []

# Loop input and append to listScores to the count of
# the CONSTANT NUM_SCORES
for i in range(0, NUM_SCORES):
    listScores.append(float(input("Enter a test score: ")))

# Display all scores in the list listScores
# with an escaped newline followed by further text on the 2nd line
print("All scores: ", listScores,
      "\nStudents who scored below 60 get 10 extra points.")
# Creates a Copy of listScores and assigns it
# to copyListScores
copyListScores = listScores.copy()

# For Loop in range of 0 to CONSTANT NUM_SCORES
# Where i is the counter
for i in range(0, NUM_SCORES):
    # if statement that checks if a index in
    # copyListScores is below the CONSTANT
    # MIN_SCORE
    if(copyListScores[i] < MIN_SCORE):
        # if true increase the score by
        # The CONSTANT ADD_SCORE
        copyListScores[i] += ADD_SCORE

# Display All scores in list copyListScores
print("All scores: ", copyListScores)
# Display Text
print("Students whose scores have changed: ")

# For Loop in range of 0 to CONSTANT NUM_SCORES
# where i is the counter
for i in range(0, NUM_SCORES):
    # if statement that checks if index i
    # in both copyListScores and ListScores
    # are not the same
    if(copyListScores[i] != listScores[i]):
        # if not the same Display the old score
        # at index of i in listScores
        # followed by the new score
        # at index of i in copyListScores
        print("Old Score: ", listScores[i], " New score: ", copyListScores[i])
