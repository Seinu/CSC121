option = input(
    "Enter A to add course, D to drop course, and E to exit: ").lower()
arrCourses = []
while(option != 'e'):
    if(option == 'a'):
        course = input("Enter course to add: ")
        if course in arrCourses:
            print("You are already registered in that course.")
        else:
            arrCourses.append(course)
            print("Course added")
    elif(option == "d"):
        course = input("Enter course to drop: ")
        if course not in arrCourses:
            print("No such registered course")
        else:
            arrCourses.remove(course)
            print("Course dropped")

    arrCourses.sort()
    print("Courses registered: ", arrCourses)
    option = input(
        "Enter A to add course, D to drop course, and E to exit: ").lower()
