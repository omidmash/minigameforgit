#testing simple functions
print("You wake up in an enclosed, dark room. The air is fresh, hinting there might be a vent of some sorts providing fresh air for you. There is a door with two buttons, A and B on it. What do you do?")
door_choice=input("Press A, B or none?\n")
if door_choice in ("A, a"):
    print ("You've chosen unwisely!")
elif door_choice in ("B", "b"):
    print ("You've chosen wisely!")
    print ("As the door wooshes open, you are greeted by a table, with a meatgrinder, a phone, and a book on it.")
    table_choice = input("Which one would you like to investigate?\n")
    if table_choice in ("meatgrinder", "the meatgrinder", "The meatgrinder", "The Meatgrinder"):
        print ("It doesn't seem to be connected to a power source, however as you press the button, it starts whirring.")
elif door_choice in ("none", "None"):
    print ("You turn around and as your eyes ")

