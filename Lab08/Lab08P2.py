def main():
    kWh, customerType = get_user_input()
    price = bill_calculator(kWh, customerType)
    print("Please pay this amount: ", price)


def get_user_input():
    kWh = 0
    while(kWh <= 0):
        kWh = int(input("Enter kilowatt hours used: "))
        if(kWh < 0):
            print("kWh cannot be negative.")
    customerType = ''
    while(customerType != 'R' and customerType != 'B'):
        customerType = input(
            "Enter R for residential customer, B for business customer: ").upper()
        if(customerType != 'R' and customerType != 'B'):
            print("Invalid customer type.")
    return kWh, customerType


def bill_calculator(kWh, customerType):
    if(customerType == "R"):
        if(kWh <= 500):
            price = kWh * 0.12
        elif(kWh > 500):
            kWh -= 500
            price = (500 * 0.12) + (kWh * 0.15)
    elif(customerType == "B"):
        if(kWh <= 800):
            price = kWh * 0.16
        elif(kWh > 800):
            kWh -= 800
            price = (800 * 0.16) + (kWh * 0.20)
    return price


main()
