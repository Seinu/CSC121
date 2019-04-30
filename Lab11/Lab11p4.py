valid = False
while valid == False:
    try:
        hotdogs = int(input("How many hotdogs do you want? "))
        valid = True
    except ValueError:
        print("Invalid input.")

valid = False
while valid == False:
    try:
        chips = int(input("How many chips do you want? "))
        valid = True
    except ValueError:
        print("Invalid input.")

valid = False
while valid == False:
    try:
        sodas = int(input("How many sodas do you want? "))
        valid = True
    except ValueError:
        print("Invalid input.")

print("Your total is $" +
      str(format((hotdogs * 2.50)+(chips * 1.50)+(sodas * 1.25), '.2f')))
