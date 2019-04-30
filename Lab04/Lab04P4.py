salary = float(input("Enter first year’s salary: "))
amountRetire = 0
for i in range(10):
    amountRetire = amountRetire + (salary * 0.05)
    print("Year: ", i + 1, "Salary: ", salary)
    print("Retirement Found Total So Far: ", amountRetire, "\n")
    salary = salary + (salary * 0.02)
