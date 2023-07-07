import pyautogui as pag
import random
import time
from datetime import datetime

# get current time
print(str(datetime.now()) + "\t>>\tStarting AFK Bot...\n")

# get current mouse position
previous_x_position, previous_y_position = pag.position()

while True:
    # current time and position of mouse
    current_x_position, current_y_position = pag.position()

    if (current_x_position, current_y_position) == (previous_x_position, previous_y_position):
        # get max screen size
        width, height = pag.size()

        # get random x and y coordinates
        new_x_position = random.randint(100, width - 100)
        new_y_position = random.randint(100, height - 100)

        # move mouse to nearby random location
        pag.moveTo(new_x_position, new_y_position, duration=0.5)
        print(str(datetime.now()) + "\t>>\tMoved mouse to: " +
              str(pag.position()) + "\n")

        previous_x_position, previous_y_position = new_x_position, new_y_position

    # sleep for 4 minutes
    time.sleep(5)
