totalwon = int(input("What is your total jackpot winnings? "))

annpayment_bfortax = totalwon / 20
print("Your annual winnings before tax is $" + format(annpayment_bfortax, '.2f'))
annpayment_aftrtax = annpayment_bfortax * 0.07
print("Your annual winnings after tax is $" + format(annpayment_aftrtax, '.2f'))

allatonce_bfortax = totalwon * 0.65
print("Your instant winnings before tax is $" + format(allatonce_bfortax, '.2f'))
allatonce_aftrtax = allatonce_bfortax * 0.7
print("Your instant winnings before tax is $" + format(allatonce_aftrtax, '.2f'))
