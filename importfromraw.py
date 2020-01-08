# simple text based game
import time
answer_a = ("A", "a")
answer_b = ("B", "b")
meatgrinder = ("meatgrinder", "Meatgrinder")
chalice = ("Chalice", "chalice")
wheel = ("Wheel", "wheel",)
yes = ("Y", "y", "yes", "Yes")
no = ("N", "n", "no", "No")

def intro():
        print("After a night of heavy drinking, you wake up in a dark room.\n"
            "You can't see an entrance or a door, but you feel a fresh breeze in the room,\n"
            "and that makes you think that the room must have a window")
        time.sleep(2)
        button_pressed = input(">>> which button do you press?\n    A.\n    B.\n")


# choice a
        if button_pressed in answer_a:
            table_choice = input("you pressed a, table bla bla, meatgrinder, chalice or wheel?\n")

            if table_choice in meatgrinder:
                print("meatgrinder, seriously?")
            elif table_choice in chalice:
                print("what is this, a church?")
            elif table_choice in wheel:
                print("huh, a wheel??")
            else:
                print("Well you have to choose or you're stuck!")



# choice B
        elif button_pressed in answer_b:
            ventilator_choice = input("bla bla ventilator, you open it and find a laser gun. Do you take it? Y/N?")
            if ventilator_choice in yes:
                gun = 1
                shoot = input("now you have a gun. Test if it works! type shoot\n")
            elif ventilator_choice in no:
                gun = 0
                print ("now what?")
            else:
                print ("enter a valid value")



# how to return?
        else:
            print("please press a button")
            intro()

intro()

