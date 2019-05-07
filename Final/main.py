# 1.	Create two Customer objects.  Since you need to pass email address to the __init__
#  method when you create a Customer object, ask the user to enter the email address of the customer first.
# 2.	For each Customer object, call the input_info method to input personal information
#  and call the verify_info method to verify peronal information.
# 3.	Write personal information of the two customers to the textfile ‘customers.txt’.
#  Each customer will occupy one line.  Personal information of each customer must be
#  written in this order: first_name, last_name, age, email, password, card_number and
#  security_code. Insert a space after each item except the security_code.  Insert a
#  newline character, i.e. ‘\n’, at the end of the line.

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
