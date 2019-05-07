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
        """
        In this method, the user enters age.  Age is invalid if it is negative or if the input string cannot 
        be converted to an integer.  If an invalid age is entered, display an error message and ask the user 
        to reenter.  Repeat this until the age is valid.  Store the valid age in the instance variable age. 
        This method has no parameter (except self) and no return value.
        """
        while(self._age < 1):
            try:
                self._age = int(input("Please enter age: "))
            except ValueError:
                print("Invalid input. Age must be an integer!")
            if(self._age < 0):
                print("Error age can't be negative!")

    def input_password(self):
        """
        In this method, the user enters a password meeting the password requirements.  The password must be 8-12 
        characters in length, and must contain at least one upper-case letter, one lower-case letter, and one 
        number.  If an invalid password is entered, display an error message and ask the user to reenter.  
        Repeat this until the password is valid.  Store the valid password in the instance variable password. 
        This method has no parameter (except self) and no return value.
        """
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
        """
        In this method, the user enters a 16-digit credit card number.  The card number is invalid if the length 
        is not 16 or if it has one or more non-digit characters.  If an invalid card number is entered, display 
        an error message and ask the user to reenter.  Repeat this until the card number is valid.  Store the 
        valid card number in the instance variable card_number. This method has no parameter (except self) and 
        no return value.
        """
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
        """
        In this method, the user enters a 3-digit credit card security code.  The security code is invalid if the 
        length is not 3 or if it has one or more non-digit characters.  If an invalid security code is entered, 
        display an error message and ask the user to reenter.  Repeat this until the security code is valid.  
        Store the valid security code in the instance variable security_code. This method has no parameter 
        (except self) and no return value.
        """
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
        """
        This method allows the user to enter first name, last name and other personal information.  First, ask 
        the user to enter first name and last name and store them in the instance variables first_name and 
        last_name.  Then call the following methods to enter other personal information: input_age, input_password, 
        input_card_number and input_security_code. This method has no parameter (except self) and no return value.
        """
        self._first_name = input("Please enter your first name.\n")
        self._last_name = input("Please enter your last name.\n")
        self.input_age()
        self.input_password()
        self.input_card_number()
        self.input_security_code()

    def verify_info(self):
        """
        This method allows the user to update any item previously entered before completing the registration. 
        First, display all instance variables.  Then ask the user to choose one item to update.  Write code or 
        call appropriate method to update the chosen item.  Repeat this until the user does not want to make 
        any more changes. This method has no parameter (except self) and no return value.
        """
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
        """
        This method creates and returns a string that consists of all personal information of the customer.  
        Data in the string must follow this order: first_name, last_name, age, email, password, card_number 
        and security_code. Insert a space after each item except the security_code.  Insert a newline 
        character, i.e. ‘\n’, at the end of the string.  The returned string will be used later to write 
        customer’s personal information to a textfile. This method has no parameter (except self).
        """
        return "%s %s %s %s %s %s %s\n" % (self._first_name, self._last_name, self._age, self._email, self._password, self._card_number, self._security_code)
