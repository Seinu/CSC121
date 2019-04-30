boolChkPatient = "y"
while(boolChkPatient != "n"):
    FPG = int(input("Enter fasting plasma glucose level: "))
    if(FPG > 125):
        print("This patient has diabetes\n")
    elif(FPG <= 125 and FPG > 100):
        print("This patient has pre-diabetes\n")
    elif(FPG <= 100):
        print("This patient has healthy fpg level\n")
    boolChkPatient = input(
        "Checking diabetes for another patient? [y/n] ").lower()
