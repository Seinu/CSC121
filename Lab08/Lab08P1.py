def main():
    kWh = get_kWh_used()
    price = bill_calculator(kWh)
    print("Please pay this amount: ", price)


def get_kWh_used():
    kWh = 0
    while(kWh <= 0):
        kWh = int(input("Enter kilowatt hours used: "))
        if(kWh < 0):
            print("kWh cannot be negative.")
    return kWh


def bill_calculator(kWh):
    if(kWh <= 500):
        price = kWh * 0.12
    elif(kWh > 500):
        kWh -= 500
        price = (500 * 0.12) + (kWh * 0.15)
    return price


main()
