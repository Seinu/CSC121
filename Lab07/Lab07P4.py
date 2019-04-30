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

def main():
    labCount = int(input("How many labs? "))
    labList = []
    for i in range(labCount):
        temp = float(input("Enter a lab score: "))
        labList.append(temp)
    print("Lab scores: ", labList)

    testCount = int(input("How many tests? "))
    testList = []
    for i in range(testCount):
        temp = float(input("Enter a test score: "))
        testList.append(temp)
    print("Test scores: ", testList)
    print("The default weights for course grade are 50% labs and 50% tests.")
    chooseweight = input(
        "Enter C to change the weights or D to use default weights: ").lower()
    if(chooseweight == "c"):
        labWeight = int(input("Enter lab percentage (without the % sign): "))
        testWeight = int(input("Enter test percentage (without the % sign): "))
        grade_calculator(labScores=labList, testScores=testList,
                         labWeight=labWeight, testWeight=testWeight)
    elif(chooseweight == "d"):
        grade_calculator(labScores=labList, testScores=testList)


def grade_calculator(labScores, testScores, labWeight=50, testWeight=50):
    labAvg = sum(labScores) / len(labScores)
    print("Lab average: ", labAvg)
    testAvg = sum(testScores) / len(testScores)
    print("Test average: ", testAvg)
    courseGrade = (labAvg * labWeight / 100) + (testAvg * testWeight / 100)
    print("Course grade: ", courseGrade)


main()
