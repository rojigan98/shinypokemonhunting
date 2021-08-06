import pyautogui
import keyboard

import time


# countdown timer
def countdown(t):
    while t: # while t > 0 for clarity
      mins = t // 60
      secs = t % 60
      timer = '{:02d}:{:02d}'.format(mins, secs)
      print(timer, end="\r") # overwrite previous line
      time.sleep(1)
      t -= 1
    print('Blast Off!!!')


count = 0

while True:
    if keyboard.is_pressed('.'):  # if key 'q' is pressed

        pyautogui.keyDown("space")



        #pyautogui.keyDown("enter")
        #countdown(1)
        #pyautogui.keyUp("enter")


        pyautogui.keyDown("9")
        time.sleep(0.3)
        pyautogui.keyUp("9")

        pyautogui.keyDown("8")
        time.sleep(0.6)
        pyautogui.keyUp("8")

        pyautogui.keyDown("a")
        pyautogui.keyUp("a")


        time.sleep(0.9)

        pyautogui.keyDown("a")
        pyautogui.keyUp("a")

        pyautogui.keyUp("space")

        count += 1

        print(count)

    elif keyboard.is_pressed('0'):  # if key 'q' is pressed

        pyautphogui.keyDown("space")

        #pyautogui.keyDown("enter")
        #countdown(1)aa
        #pyautogui.keyUp("enter")

        print('should go down here')
        pyautogui.keyDown("9")
        pyautogui.keyUp("9")
        time.sleep(0.2)

        print('should be down by now')

        pyautogui.keyDown("l")
        pyautogui.keyUp("l")
        time.sleep(0.2)


        pyautogui.keyDown("a")
        pyautogui.keyUp("a")
        time.sleep(0.2)

        pyautogui.keyDown("a")
        pyautogui.keyUp("a")
        time.sleep(0.2)

        pyautogui.keyDown("a")
        pyautogui.keyUp("a")
        time.sleep(0.2)

        pyautogui.keyUp("space")
        print('You Pressed A Key!')

        # break  # finishing the loop
    elif keyboard.is_pressed('h'):
        print('abort')
        break
