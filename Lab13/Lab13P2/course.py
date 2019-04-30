class Course:

    def __init__(self, c_code, c_max_size):

        # initialize self.code to c_code
        self.code = c_code
        # initialize self.max_size to c_max_size
        self.max_size = c_max_size
        # initialize self.enrollment to 0
        self.enrollment = 0

    def add_student(self):

        # if self.enrollment is less than self.max_size, increase self.enrollment by 1 and display "one student added"
        if(self.enrollment < self.max_size):
            self.enrollment += 1
            print("one student added")
        # else display "Course already full"
        else:
            print("Course already full")

    def drop_student(self):

        # if self.enrollment is greater than 0, decrease self.enrollment by 1 and display "One student dropped"
        if(self.enrollment > 0):
            self.enrollment -= 1
            print("One student dropped")
        # else display "Course is empty"
        else:
            print("Course is empty")
