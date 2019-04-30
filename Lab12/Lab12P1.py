def main():
    """ simulate self checkout system of grocery store """
    print("elcome to the self-checkout system of Woke-mart")
    count, total = scan_prices()
    total = discount(count, total)
    count, total = promotion(count, total)
    make_payment(total)


def scan_prices():
    """ gets item prices and return total """
    total, count = 0.0, 0
    price = 1.0

    while(price != 0):
        try:
            price = float(input("Enter price of next item [or 0 to stop]: "))
        except ValueError:
            print("Invalid input. Item Price must be a number")
            continue
        if(price > 0):
            total = total + price
            count = count + 1
            print("Number of items: ", count, "Total: ${:.2f}".format(total))
        elif(price < 0):
            print("Price cannt be negative")

    return count, total


def discount(count, total):
    """ give 10% discount if customer buys 10 items or more """
    if(count >= 10):
        print("you've got 10% discount for buying 10 items of more. ")
        total = total * 0.9
        print("Number of items: ", count, "Total: ${:.2f}".format(total))
        return total
    return total


def promotion(count, total):
    """ customer can buy %50 gift card for $40 if total is $50 or higher """
    if(total > 50):
        answer = ""
        while(answer != "y" and answer != "n"):
            answer = input("Do you want to buy a $50 gift card for $40? [y/n]")
            if(answer != "y" and answer != "n"):
                print("invalid input")
        if(answer == "y"):
            count += 1
            total = total + 40.0
            print("Number of items: ", count, "Total: ${:.2f}".format(total))

    return count, total


def make_payment(total):
    """ Let customer choose payment type """
    answer = 0
    while(answer != 1 and answer != 2):
        try:
            answer = int(input("Enter 1 for cash, 2 for debit: "))
        except ValueError:
            continue

        if(answer != 1 and answer != 2):
            print("invalid input")
    if(answer == 1):
        pay_cash(total)
    elif(answer == 2):
        pay_debit(total)


def pay_cash(total):
    """ Process cash payment """
    totalpay = 0
    while(totalpay < total):
        try:
            tens = int(input("How many $10 bills are you going to pay? "))
        except ValueError:
            print("invalid input must be an integer. Value set to 0")
            tens = 0

        try:
            fives = int(input("How many $5 bills are you going to pay? "))
        except ValueError:
            print("invalid input must be an integer. Value set to 0")
            fives = 0

        try:
            ones = int(input("How many $1 bills are you going to pay? "))
        except ValueError:
            print("invalid input must be an integer. Value set to 0")
            ones = 0

        totalpay = (tens * 10) + (fives * 5) + (ones * 1)
        if(totalpay < total):
            print("Error: Total cash payment less than balance. Please reenter.")        
        if(totalpay > total):
            print("Total cash paid: ", totalpay)
            print("Thank you for your payment.")
            change = totalpay - total
            print("Change: ${:.2f}".format(change))


def pay_debit(total):
    """ process debit payment """
    input("Please enter a 16-digit card number: ")
    input("Please enter 4-digit pin: ")
    payment = 0
    while(payment < total):
        try:
            payment = float(input("Please enter payment amount: "))
        except ValueError:
            print("Invalid input. Item Price must be a float")
            continue
        if(payment<total):
            print("ERROR: Payment amount cannot be smaller than balance")

    print("Thank you for your payment.")
    if(payment > total):
        change = payment - total
        print("Change: ${:.2f}".format(change))


main()
