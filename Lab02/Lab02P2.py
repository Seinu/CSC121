lab01 = int(input("What is your first lab score?"))
lab02 = int(input("What is your second lab score?"))
lab03 = int(input("What is your third lab score?"))
test01 = int(input("What is your first test score?"))
test02 = int(input("What is your second test score?"))
labavg = (lab01 + lab02 + lab03) / 3
print("Your average lab score is " + str(labavg))

testavg = (test01 + test02) / 2
print("Your average test score is " + str(testavg))

grade = (labavg * 0.55) + (testavg * 0.45)
print("Your grade is " + str(grade))
