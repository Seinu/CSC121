# CONSTANTS
p = 4
n = 6

# Create Empty List Inside of a List
powMatrix = [[]]

# Counter for list index
counter = 0

# For Loop for calculating the numbers to get the power of
# Uses the CONSTANT n for the number
# n + 1 is required for proper loop through range

for i in range(2, n+1):
    # Second For Loop for calculatating powers of the numbers
    # uses CONSTANT p for power
    # p + 1 is required for proper loop through range
    for x in range(1, p+1):
        # appends i to the power of x
        # where i is the number to get the power of
        # and x is the power
        # uses variable counter for proper indexing
        powMatrix[counter].append(i ** x)
    # increase index counter for proper append
    counter += 1
    # if i is equal to the last number to get power of
    # Then break out of loop
    if(i == n):
        break
    # append another empty list to the list powMatrix

    # TODO consider removing break from the above if
    # and change if to i <= n and just directly append
    # an Empty List to powMatrix
    powMatrix.append([])

# Display list at index 0 of powMatrix which is power of 2
# Display list at index 0 of powMatrix which is power of 3
# Display full powers Matrix powMatrix
print("Powers of 2: ", powMatrix[0])
print("Powers of 3 ", powMatrix[1])
print("Matrix: ", powMatrix)
