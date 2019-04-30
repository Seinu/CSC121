s_e = input("Enter S for standard shipping, E for express: ").upper()
weight = float(input("Enter weight (lbs): "))
if(s_e == "S"):
    if(weight <= 4.0):
        rate = 1.05
    elif(weight > 4.0 and weight <= 8.0):
        rate = 0.95
    elif(weight > 8.0 and weight <= 15.0):
        rate = 0.85
    else:
        rate = 0.80

if(s_e == "E"):
    if(weight <= 2.0):
        rate = 3.25
    elif(weight > 2.0 and weight <= 5.0):
        rate = 2.95
    elif(weight > 5.0 and weight <= 10.0):
        rate = 2.75
    else:
        rate = 2.55

shipCharge = weight * rate
print("Shipping charge:  " + str(shipCharge))