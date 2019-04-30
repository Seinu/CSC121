def main():
    kWh = int(input("Enter kilowatt hours used: "))
    bill_calculator(kWh)


def bill_calculator(kWh):
    if(kWh <= 500):
        price = kWh * 0.12
    elif(kWh > 500):
        kWh -= 500
        price = (500 * 0.12) + (kWh * 0.15)
    print("Please pay this amount: ", price)


main()
