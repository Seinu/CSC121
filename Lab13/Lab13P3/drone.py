class Drone:

    def __init__(self):
        # initialize self.__speed to 0
        self.__speed = 0
        # initialize self.__height to 0
        self.__height = 0

    def accelerate(self):
        # increase self.__speed by 10
        self.__speed += 10

    def decelerate(self):
        # decrease self.__speed by 10
        self.__speed -= 10
        # if self.s__peed is less than 0, change it to 0
        if(self.__speed < 0):
            self.__speed = 0

    def ascend(self):
        # increase self.__height by 10
        self.__height += 10

    def descend(self):
        # decrease self.__height by 10
        self.__height -= 10
        # if self.__height is less than 0, change it to 0
        if(self.__height < 0):
            self.__height = 0

    def __str__(self):
        return "Speed: " + str(self.__speed) + "  Height: " + str(self.__height)
