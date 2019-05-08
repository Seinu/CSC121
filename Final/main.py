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

from customer import Customer


def main():

    print("Customer 1")
    email = input("Please enter a email: ")
    customer1 = Customer(email)
    customer1.input_info()
    customer1.verify_info()

    print("Registration and verification completed for this customer.\n")

    print("Customer 2")
    email = input("Please enter a email: ")
    customer2 = Customer(email)
    customer2.input_info()
    customer2.verify_info()

    f = open("customers.txt", "w")
    f.write("%s%s" % (customer1.output_info(), customer2.output_info()))
    f.close()


main()
