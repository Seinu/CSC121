listA = []
for i in range(5, 22, 4):
    listA.append(i)
print(listA)
print("Elements in the first list:")
for i in range(0, len(listA)):
    print(listA[i])

listB = []
for i in range(26, 4, -7):
    listB.append(i)
print(listB)
total = 0
for i in range(0, len(listB)):
    total = total + listB[i]
print(total)
