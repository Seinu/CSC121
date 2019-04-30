r_b = input("Enter R for residential customer or B for business customer: ").upper()
gallons = float(input("How many gallons of water were used? "))
if(r_b == "R"):
    if(gallons <= 6000):
        total = gallons * 0.005
    elif(gallons > 6000):
        total = ((gallons - 6000) * 0.007) + (6000 * 0.005)
    else:
        print("There was an error")

if(r_b == "B"):
    if(gallons <= 8000):
        total = gallons * 0.006
    elif(gallons > 8000):
        total = ((gallons - 8000) * 0.008) + (8000 * 0.006)
    else:
        print("There was an error")

print("Please pay this amount: $" + str(total))