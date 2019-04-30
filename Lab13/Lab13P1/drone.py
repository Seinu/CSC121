class Drone:

    def __init__(self):
        # initialize self.speed to 0
        self.speed = 0
        # initialize self.height to 0
        self.height = 0

    def accelerate(self):
        # increase self.speed by 10
        self.speed += 10

    def decelerate(self):
        # decrease self.speed by 10
        self.speed -= 10
        # if self.speed is less than 0, change it to 0
        if(self.speed < 0):
            self.speed = 0

    def ascend(self):
        # increase self.height by 10
        self.height += 10

    def descend(self):
        # decrease self.height by 10
        self.height -= 10
        # if self.height is less than 0, change it to 0
        if(self.height < 0):
            self.height = 0
