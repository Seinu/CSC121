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

option = input(
    "Enter A to add course, D to drop course, and E to exit: ").lower()
arrCourses = []
while(option != 'e'):
    if(option == 'a'):
        course = input("Enter course to add: ")
        if course in arrCourses:
            print("You are already registered in that course.")
        else:
            arrCourses.append(course)
            print("Course added")
    elif(option == "d"):
        course = input("Enter course to drop: ")
        if course not in arrCourses:
            print("No such registered course")
        else:
            arrCourses.remove(course)
            print("Course dropped")

    arrCourses.sort()
    print("Courses registered: ", arrCourses)
    option = input(
        "Enter A to add course, D to drop course, and E to exit: ").lower()
