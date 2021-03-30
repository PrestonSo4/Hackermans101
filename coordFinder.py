'''
Since the coords for PYautoGUI differ for each OS, I created this program to easily find coords.
'''
import pyautogui, time
print("Press \"CTRL + C\" when you want to quit the program")
while True:
    print(pyautogui.position())
    time.sleep(1.5)

#My coords:
#   --Sign-in button: (1042, 648)
#   --1st vid like button: (580, 90) 
#   --2nd vid like button: (872, 910)
#   --3rd vid like button: (1142, 910)
#   --4th vid like button: (1422, 910)
# NOTE: You may also want to add roughly 10-20 pixels extra on the Y-Coord b/c the message below the search bar
#...
#...
#...