foodcharge = float(input("What is your food charge? "))
tax = format((foodcharge * 0.07), '.2f')
print(tax)

tip = format((foodcharge * 0.18), '.2f')
print(tip)

print("Your total is $"+str(foodcharge+float(tax)+float(tip)))
