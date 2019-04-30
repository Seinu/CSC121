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

from course import Course


def main():

    # input course code and max size
    c_code = input("Enter course code: ")
    c_max_size = int(input("Enter maximum class size: "))
    # create Course object, pass course code and max size as arguments
    course = Course(c_code, c_max_size)
    # initialize choice to 4
    choice = 4

    while(choice != 0):

        # input choice
        choice = int(input(
            "Enter 1 for add student, 2 for drop student, 3 for course info, 0 for exit: "))

        # if choice is 1, call add_student method of Course object and display enrollment of Course object
        if(choice == 1):
            course.add_student()
            print("Enrollment: ", course.enrollment)

        # if choice is 2, call drop_student method of Course object and display enrollment of Course object
        if(choice == 2):
            course.drop_student()
            print("Enrollment: ", course.enrollment)

        # if choice is 3, display course code, max size and enrollment of Course object
        if(choice == 3):
            print("Course code: ", course.code)
            print("Maximum class size: ", course.max_size)
            print("Enrollment: ", course.enrollment)


main()
