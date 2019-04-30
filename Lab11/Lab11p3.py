try:
    hotdogs = int(input("How many hotdogs do you want? "))
except ValueError:
    print("Invalid input. Number of hotdogs set to 0.")
    hotdogs = 0


try:
    chips = int(input("How many chips do you want? "))
except ValueError:
    print("Invalid input. Number of chips set to 0.")
    chips = 0

try:
    sodas = int(input("How many sodas do you want? "))
except ValueError:
    print("Invalid input. Number of sodas set to 0.")
    sodas = 0

print("Your total is $" +
      str(format((hotdogs * 2.50)+(chips * 1.50)+(sodas * 1.25), '.2f')))
