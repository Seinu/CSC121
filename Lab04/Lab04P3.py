height = float(input("Enter initial height: "))
bounceIndex = float(input("Enter bounciness index: "))
numBounceCount = int(
    input("Enter number of times the ball is allowed to bounce: "))
for i in range(numBounceCount):
    height = height * bounceIndex
    print("Number of bounces: ", i + 1, " Height: ", height)
