string = input("Enter a string: ")
print(string)
string = string.upper()
charList = [[],[]]
for c in string:
  if(c.isalpha() == True):
    if(c not in charList[0]):
      charList[0].append(c)
      charList[1].append(1)
    elif(c in charList[0]):
      tmp = charList[0].index(c)
      charList[1][tmp] += 1

for i in range(0, len(charList[0])):
  print(charList[0][i], charList[1][i])
