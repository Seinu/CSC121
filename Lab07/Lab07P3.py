def main():

    kWh = int(input("Enter kilowatt hours used: "))
    customerType = input(
        "Enter R for residential customer, B for business customer: ").lower()
    bill_calculator(customerType=customerType, kWh=kWh)


def bill_calculator(kWh, customerType):
    if(customerType == "r"):
        if(kWh <= 500):
            price = kWh * 0.12
        elif(kWh > 500):
            kWh -= 500
            price = (500 * 0.12) + (kWh * 0.15)
    elif(customerType == "b"):
        if(kWh <= 800):
            price = kWh * 0.16
        elif(kWh > 800):
            kWh -= 800
            price = (800 * 0.16) + (kWh * 0.20)
    print("Please pay this amount: ", price)


main()
