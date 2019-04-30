import currency

def main():
  print("Converting US Dollar to a foreign currency.")
  curr,dollar = 0,-1
  while(curr != 1 and curr != 2 and curr != 3):
    curr =  int(input("Enter 1 for Euro, 2 for Japanese Yen, 3 for Mexican Peso: "))
    if(curr != 1 and curr != 2 and curr != 3):
      print("Error: Invalid Choice")

  while(dollar < 0):
    dollar = int(input("Enter US Dollar: "))
    if(dollar < 0):
      print("Error: US Dollar cannot be negative.")
      

  if(curr == 1):
    print("It is converted to ", currency.to_euro(dollar), " Euro")
  if(curr == 2):
    print("It is converted to ", currency.to_yen(dollar), " Yen")
  if(curr == 3):
    print("It is converted to ", currency.to_peso(dollar), " peso")

main()