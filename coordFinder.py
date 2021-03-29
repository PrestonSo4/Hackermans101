'''
Since the coords for PYautoGUI differ for each OS, I created this program to easily find coords.
'''
import pyautogui, keyboard, time
print("Press \"CTRL + C\" when you want to quit the program")
while True:
    print(pyautogui.position())
    time.sleep(1.5)

#My coords:
#   --Sign-in button: (1042, 648)
#   --1st vid like button: (580, 890)
#   --2nd vid like button: (872, 890)
#   --3rd vid like button: (1142, 890)
#   --4th vid like button: (1422, 890)
#...
#...
#...