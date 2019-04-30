showonly = int(input("How many people wqnt to watch just the 3d shark show? "))
admitonly = int(input("How many people just want admission to the aquarium? "))
both = int(input("How many people want both? "))

showonly = showonly * 8
admitonly = admitonly * 14
both = (both * (14 + 8)) * 0.75
total = showonly + admitonly + both
print("The group total is $" + format(total, '.2f'))
