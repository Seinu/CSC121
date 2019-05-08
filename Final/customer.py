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

import re


class Customer:

    def __init__(self, email):
        self._email = email
        self._first_name = ""
        self._last_name = ""
        self._age = 0
        self._password = ""
        self._card_number = ""
        self._security_code = ""

    def input_age(self):
        while(self._age < 1):
            try:
                self._age = int(input("Please enter age: "))
            except ValueError:
                print("Invalid input. Age must be an integer!")
            if(self._age < 0):
                print("Error age can't be negative!")

    def input_password(self):
        correct = False

        while(correct == False):
            print("Your password must be 8-12 characters long containing at least one upper-case letter, one lower-case letter, and one number.")
            self._password = input("Please enter a password: ")
            if (len(self._password) < 8 or len(self._password) > 12):
                print("Error password must be between 8 and 12 characters")
            elif not re.search("[A-Z]", self._password):
                print("Error password must contain atleast one uppercase letter")
            elif not re.search("[a-z]", self._password):
                print("Error password must contain atleast one lowercase letter")
            elif not re.search("[0-9]", self._password):
                print("Error password must contain atleast one number")
            else:
                correct = True

    def input_card_number(self):
        correct = False
        while(correct == False):
            self._card_number = input(
                "Please enter your 16-digit card number: ")
            if(len(self._card_number) != 16):
                print("Error card number must have 16 digits")
            elif not self._card_number.isdigit():
                print("Error invalid card number, card number must be all numbers")
            else:
                correct = True

    def input_security_code(self):
        correct = False
        while(correct == False):
            self._security_code = input(
                "Please enter your 3-digit security code: ")
            if(len(self._security_code) != 3):
                print("Error security code must be exactly 3 digits")
            elif not self._security_code.isdigit():
                print("Error invalid security code, security code must be all numbers")
            else:
                correct = True

    def input_info(self):
        self._first_name = input("Please enter your first name.\n")
        self._last_name = input("Please enter your last name.\n")
        self.input_age()
        self.input_password()
        self.input_card_number()
        self.input_security_code()

    def verify_info(self):
        verify = False
        while(verify == False):
            print("Email: ", self._email, "\n",
                  "First Name: ", self._first_name, "\n",
                  "Last Name: ", self._last_name, "\n",
                  "Age: ", self._age, "\n",
                  "Password: ", self._password, "\n",
                  "Card Number: ", self._card_number, "\n",
                  "Security Code: ", self._security_code, "\n")
            tmp = input("Would you like to make changes (y/n): ").lower()
            if(tmp == "n"):
                verify = True
                break
            elif(tmp == "y"):
                temp = input("Enter E to change email,\nF to change first name,\nL to change last name,\nA to change age,\nP to change password,\nC to change card number,\nor S to change security code\n(E/F/L/A/P/C/S)").upper()
                if(temp == "F"):
                    self._first_name = input("Please enter your first name")
                elif(temp == "L"):
                    self._first_name = input("Please enter your first name")
                elif(temp == "A"):
                    self._age = 0
                    self.input_age()
                elif(temp == "P"):
                    self._password = ""
                    self.input_password()
                elif(temp == "C"):
                    self._card_number = ""
                    self.input_card_number()
                elif(temp == "S"):
                    self._security_code = ""
                    self.input_security_code()
                elif(temp == "E"):
                    self._email = input("Please enter a email: ")

    def output_info(self):
        return "%s %s %s %s %s %s %s\n" % (self._first_name, self._last_name, self._age, self._email, self._password, self._card_number, self._security_code)
