class Customer:

    def __init__(self, email):
        self.__email = email
        first_name = ""
        last_name = ""
        age = 0
        password = ""
        card_number = ""
        security_code = ""

    def input_age(self):
        """
        In this method, the user enters age.  Age is invalid if it is negative or if the input string cannot 
        be converted to an integer.  If an invalid age is entered, display an error message and ask the user 
        to reenter.  Repeat this until the age is valid.  Store the valid age in the instance variable age. 
        This method has no parameter (except self) and no return value.
        """

    def input_password(self):
        """
        n this method, the user enters a password meeting the password requirements.  The password must be 8-12 
        characters in length, and must contain at least one upper-case letter, one lower-case letter, and one 
        number.  If an invalid password is entered, display an error message and ask the user to reenter.  
        Repeat this until the password is valid.  Store the valid password in the instance variable password. 
        This method has no parameter (except self) and no return value.
        """

    def input_card_number(self):
        """
        In this method, the user enters a 16-digit credit card number.  The card number is invalid if the length 
        is not 16 or if it has one or more non-digit characters.  If an invalid card number is entered, display 
        an error message and ask the user to reenter.  Repeat this until the card number is valid.  Store the 
        valid card number in the instance variable card_number. This method has no parameter (except self) and 
        no return value.
        """

    def input_security_code(self):
        """
        In this method, the user enters a 3-digit credit card security code.  The security code is invalid if the 
        length is not 3 or if it has one or more non-digit characters.  If an invalid security code is entered, 
        display an error message and ask the user to reenter.  Repeat this until the security code is valid.  
        Store the valid security code in the instance variable security_code. This method has no parameter 
        (except self) and no return value.
        """

    def input_info(self):
        """
        This method allows the user to enter first name, last name and other personal information.  First, ask 
        the user to enter first name and last name and store them in the instance variables first_name and 
        last_name.  Then call the following methods to enter other personal information: input_age, input_password, 
        input_card_number and input_security_code. This method has no parameter (except self) and no return value.
        """

    def verify_info(self):
        """
        This method allows the user to update any item previously entered before completing the registration. 
        First, display all instance variables.  Then ask the user to choose one item to update.  Write code or 
        call appropriate method to update the chosen item.  Repeat this until the user does not want to make 
        any more changes. This method has no parameter (except self) and no return value.
        """

    def output_info(self):
        """
        This method creates and returns a string that consists of all personal information of the customer.  
        Data in the string must follow this order: first_name, last_name, age, email, password, card_number 
        and security_code. Insert a space after each item except the security_code.  Insert a newline 
        character, i.e. ‘\n’, at the end of the string.  The returned string will be used later to write 
        customer’s personal information to a textfile. This method has no parameter (except self).
        """
