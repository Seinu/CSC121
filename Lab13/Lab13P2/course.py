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

class Course:

    def __init__(self, c_code, c_max_size):

        # initialize self.code to c_code
        self.code = c_code
        # initialize self.max_size to c_max_size
        self.max_size = c_max_size
        # initialize self.enrollment to 0
        self.enrollment = 0

    def add_student(self):

        # if self.enrollment is less than self.max_size, increase self.enrollment by 1 and display "one student added"
        if(self.enrollment < self.max_size):
            self.enrollment += 1
            print("one student added")
        # else display "Course already full"
        else:
            print("Course already full")

    def drop_student(self):

        # if self.enrollment is greater than 0, decrease self.enrollment by 1 and display "One student dropped"
        if(self.enrollment > 0):
            self.enrollment -= 1
            print("One student dropped")
        # else display "Course is empty"
        else:
            print("Course is empty")
