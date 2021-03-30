import selenium, time, pyautogui, webbrowser, random, getpass, win32api, win32con, keyboard
from selenium import webdriver
from getpass import getpass
likeX, likeY = 580, 910 #You may need to change ur coords. Use coordFinder.py to find ur coords for ur OS. -Preston 👍
def pClick(): #I created this function because it's faster than >>>pygautogui.click()
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) #MAKE SURE YOU HAVE WIN32API INSTALLED. Type: >pip install pywin32
    time.sleep(0.0001)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
email = 's-sop@bsd405.org' #                       --If you are just spamming, put in ur BSD email here *I make this for ease of access
#email = input('Enter your email: ')               --This is replace this for the line above
#psswrd = input('Enter your password: ')
psswrd = getpass('Enter your password: ') #       --USE THIS IF UR SHARING UR SCREEN OR SHOWING FRIENDS. FOR TESTING, USE THE LINE ABOVE SO YOU CAN CHECK UR PSSWORD AND SAVE TIME
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://login.microsoftonline.com/common/oauth2/v2.0/authorize?response_type=code&response_mode=query&client_id=f1143447-b07a-4557-b878-b78df8d45c13&redirect_uri=https://flipgrid.com/auth/sso&scope=User.Read&prompt=select_account&state=eyJyZWRpcmVjdF90byI6Ii8wZDRiMWY3Nz9yZW1lbWJlcj10cnVlIiwicHJvdmlkZXIiOiJtaWNyb3NvZnQiLCJyZW1lbWJlcl9tZSI6dHJ1ZSwidG9waWNfaWQiOjIxMTY1OTQwfQ==&sso_reload=true')
time.sleep(3)
loginMS = driver.find_element_by_xpath('//*[@id="i0116"]')
loginMS.send_keys(email)
nextMS = driver.find_element_by_id('idSIButton9')
nextMS.click()
psswrdMS = driver.find_element_by_id('i0118')
psswrdMS.send_keys(psswrd)
pyautogui.moveTo(1042, 648, duration=1, tween=pyautogui.easeInOutQuad)# Makesure you have Pyautogui installed. Type: >pip install pyautogui
#You may need to change ur coords. Use coordFinder.py to find ur coords for ur OS. -Preston 👍
print('moved to!')
time.sleep(1)
pClick()
time.sleep(2)
pClick()
print('clicked!')
time.sleep(3)
for i in range(1000000):
    driver.get('https://flipgrid.com/0d4b1f77')
    time.sleep(0.6)#buffer for page to load
    """
    if pyautogui.position() != (likeX, likeY):
        move = pyautogui.moveTo(likeX, likeY, duration=0, tween=pyautogui.easeInOutQuad)
    #You may need to change ur coords. Use coordFinder.py to find ur coords for ur OS. -Preston 👍
    pClick()
    """
    pyautogui.moveTo(585, 910, duration=0, tween=pyautogui.easeInOutQuad) #First like box (Asher's)
    pClick()
    pyautogui.moveTo(872, 910, duration=0, tween=pyautogui.easeInOutQuad) #Second like box (Laura Walter's)
    pClick()
    pyautogui.moveTo(1142, 910, duration=0, tween=pyautogui.easeInOutQuad) #Third like box (Zaeemah's)
    pClick()
    pyautogui.moveTo(1422, 910, duration=0, tween=pyautogui.easeInOutQuad) #Fourth like box (Zaeemah's Example)
    pClick()
    #"""
    #If you want to like only one box, just comment out lines 40-47 and replace the likeX and likeY coords to the box's respective coords.
driver.close()