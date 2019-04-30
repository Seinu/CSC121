string = input("Enter a string: ")

string = string.upper()
charDict = {}
for c in string:
  if(c.isalpha() == True):
    if(c not in charDict):
      charDict[c] = 1
    elif(c in charDict):
      charDict[c] += 1

print("Dictionary", charDict)

letter = input("Choose a letter: ").upper()
print("Frequency count of that letter: ", charDict[letter])
charDict.pop(letter, None)
print("Dictionary after that letter removed: ", charDict)
charList = sorted(list(charDict.keys()))
print("Letters sorted: ", charList)