class Course:

    def __init__(self, c_code, c_max_size):

        # initialize self.__code to c_code
        self.__code = c_code
        # initialize self.__max_size to c_max_size
        self.__max_size = c_max_size
        # initialize self.__enrollment to 0
        self.__enrollment = 0

    def add_student(self):

        # if self.__enrollment is less than self.__max_size, increase self.__enrollment by 1 and display "one student added"
        if(self.__enrollment < self.__max_size):
            self.__enrollment += 1
            print("one student added")
        # else display "Course already full"
        else:
            print("Course already full")

    def drop_student(self):

        # if self.__enrollment is greater than 0, decrease self.__enrollment by 1 and display "One student dropped"
        if(self.__enrollment > 0):
            self.__enrollment -= 1
            print("One student dropped")
        # else display "Course is empty"
        else:
            print("Course is empty")

    def get_course_code(self):
        # return self.__code
        return self.__code

    def get_enrollment(self):
        # return self.__enrollment
        return self.__enrollment

    def get_max_size(self):
        # return self.__max_size
        return self.__max_size

    def set_max_size(self, new_max_size):

        # if new_max_size < 0, display "Maximum class size cannot be negative."
        if(new_max_size < 0):
            print("Maximum class size cannot be negative.")
        # elif new_max_size < self.__enrollment, display "Maximum class size cannot be lower than current enrollment."
        elif(new_max_size < self.__enrollment):
            print("Maximum class size cannot be lower than current enrollment.")
        # else change self.__max_size to new_max_size and display "Maximum class size changed."
        else:
            self.__max_size = new_max_size
            print("Maximum class size changed.")
