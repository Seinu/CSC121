from drone import Drone


def main():

    # create Drone object
    drone = Drone()

    # set choice to 5
    choice = 5

    while(choice != 0):

        # input choice
        choice = int(input(
            "Enter 1 for accelerate, 2 for decelerate, 3 for ascend, 4 for descend, 0 for exit: "))

        # if choice is 1, call accelerate method of drone object
        if(choice == 1):
            drone.accelerate()

        # if choice is 2, call decelerate method of drone object
        if(choice == 2):
            drone.decelerate()

        # if choice is 3, call ascend method of drone object
        if(choice == 3):
            drone.ascend()

        # if choice is 4, call descend method of drone object
        if(choice == 4):
            drone.descend()

        if(choice == 0):
            exit()

        # display speed and height of drone object
        print("Speed: ", drone.speed, "Height:  ", drone.height)


main()
