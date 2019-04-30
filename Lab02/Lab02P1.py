hotdogs = int(input("How many hotdogs do you want?"))
chips = int(input("How many chips do you want?"))
sodas = int(input("How many sodas do you want?"))
print("Your total is $" + str(format((hotdogs * 2.50)+(chips * 1.50)+(sodas * 1.25), '.2f')))
