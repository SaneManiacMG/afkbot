import pyautogui as pag
import random
import time
from datetime import datetime

# turn off pyautogui fail safe
pag.FAILSAFE = False

# get current time
print(str(datetime.now()) + "\t>>\tStarting AFK Bot...\n")

# get current mouse position
previous_x_position, previous_y_position = pag.position()
print(str(datetime.now()) + "\t>>\tInitial mouse position: " +
      str(pag.position()) + "\n")
time.sleep(5)

while True:
    # current time and position of mouse
    current_x_position, current_y_position = pag.position()
    print(str(datetime.now()) +
          "\t>>\tCurrent mouse position: " + str(pag.position()))

    if (current_x_position, current_y_position) == (previous_x_position, previous_y_position):
        # get max screen size
        width, height = pag.size()

        # get random x and y coordinates
        new_x_position = current_x_position + random.randint(-250, 250)
        new_y_position = current_y_position + random.randint(-250, 250)

        # move mouse to nearby random location
        pag.moveTo(new_x_position, new_y_position, duration=0.5)
        print(str(datetime.now()) + "\t>>\tMoved mouse to: " +
              str(pag.position()) + "\n")
    else:
        new_x_position = current_x_position
        new_y_position = current_y_position

    previous_x_position, previous_y_position = new_x_position, new_y_position

    # sleep for 3 minutes
    time.sleep(180)
