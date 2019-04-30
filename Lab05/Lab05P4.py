import random
listA = []
listB = []
for i in range(0, 5):
    listA.append(random.randint(1, 9))
    listB.append(random.randint(2, 8))
print("First list: ", listA)
print("Second list: ", listB)
print("Larger number in each comparison:")
for i in range(0, 5):
    if(listA[i] > listB[i]):
        print(listA[i])
    elif((listA[i] < listB[i])):
        print(listB[i])
