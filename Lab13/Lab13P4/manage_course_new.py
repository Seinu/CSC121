from course import Course


def main():

    # input course code and max size
    c_code = input("Enter course code: ")
    c_max_size = int(input("Enter maximum class size: "))
    # create Course object, pass course code and max size as arguments
    course = Course(c_code, c_max_size)
    # initialize choice to 5
    choice = 5

    while choice != 0:

        # input choice
        choice = int(input(
            "Enter 1 for add student, 2 for drop student, 3 for course info, 4 for change maximum class size, 0 for exit: "))

        # if choice is 1, call add_student method of Course object and display enrollment of Course object
        if(choice == 1):
            course.add_student()
            print("Enrollment: ", course.get_enrollment())

        # if choice is 2, call drop_student method of Course object and display enrollment of Course object
        if(choice == 2):
            course.drop_student()
            print("Enrollment: ", course.get_enrollment())

        # if choice is 3, display course code, max size and enrollment of Course object
        if(choice == 3):
            print("Course code: ", course.get_course_code())
            print("Maximum class size: ", course.get_max_size())
            print("Enrollment: ", course.get_enrollment())

        # elif choice is 4 input new size and call set_max_size method of Course object
        if(choice == 4):
            c_max_size = int(input("Enter new maximum class size: "))
            course.set_max_size(c_max_size)


main()
