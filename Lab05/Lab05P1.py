numL = []
boolCont = 'y'
avg = 0.0
while(boolCont == 'y'):
    numL.append(int(input("Enter an integer from 1 to 10: ")))
    boolCont = input("Enter another integer? [y/n] ").lower()

for i in range(0, len(numL)):
    avg += numL[i]

avg = avg / len(numL)

print("Number list: ", numL)
print("Average: ", avg)

if(avg > 7):
    for i in range(0, len(numL)):
        numL[i] = numL[i] - 1
print("Modified Number list: ", numL)
