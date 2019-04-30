outfile = open("water.txt", "w")
for i in range(0,4):
  accountNum = input("Enter account number: ")
  custType = input("Enter R for residential, B for business: ").upper()
  galUsed = input("Enter number of gallons used: ")
  outfile.write("{0} {1} {2}\n".format(accountNum, custType, galUsed))

outfile.close()
