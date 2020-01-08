#testing simple functions
import time
answer_A = ("A", "a")
answer_B = ("B", "b")


def intro():
    print ("You wake up in an enclosed, dark room. The air is fresh, hinting there might be a vent of some sorts providing fresh air for you. There is a door with two buttons, A and B on it. What do you do?")
    door_choice=input("Press A, B or none?\n")
    if door_choice in ("A, a"):
            print ("You've chosen unwisely!")
    elif door_choice in ("B", "b"):
            print ("You've chosen wisely!")
    elif door_choice in ("none", "None"):
            print ("You turn around and as your eyes ")
