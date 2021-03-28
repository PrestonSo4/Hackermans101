import selenium, time, pyautogui, webbrowser, random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from getpass import getpass
email = 's-sop@bsd405.org'
#email = input('Enter your email: ')= ''
psswrd = input('Enter your password: ')
driver = webdriver.Chrome()
#driver.get('https://flipgrid.com/0d4b1f77')
driver.get('https://login.microsoftonline.com/common/oauth2/v2.0/authorize?response_type=code&response_mode=query&client_id=f1143447-b07a-4557-b878-b78df8d45c13&redirect_uri=https://flipgrid.com/auth/sso&scope=User.Read&prompt=select_account&state=eyJyZWRpcmVjdF90byI6Ii8wZDRiMWY3Nz9yZW1lbWJlcj10cnVlIiwicHJvdmlkZXIiOiJtaWNyb3NvZnQiLCJyZW1lbWJlcl9tZSI6dHJ1ZSwidG9waWNfaWQiOjIxMTY1OTQwfQ==&sso_reload=true')
email = "s-sop@bsd405.org"
#joinMS = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div/div[2]/div/div[1]/button[2]')
#joinMS.click()
time.sleep(2)
loginMS = driver.find_element_by_name('loginfmt')
loginMS.send_keys(email)
nextMS = driver.find_element_by_id('idSIButton9')
nextMS.click()
psswrdMS = driver.find_element_by_id('i0118')
psswrdMS.send_keys(psswrd)
pyautogui.moveTo(545, 652, duration=1, tween=pyautogui.easeInOutQuad)
print('moved to!')
time.sleep(1)
pyautogui.click()
time.sleep(1.5)
pyautogui.click()
print('clicked!')
time.sleep(3)
driver.get('https://flipgrid.com/0d4b1f77')
move = pyautogui.moveTo(545, 932, duration=1, tween=pyautogui.easeInOutQuad)
for i in range(1000000):
    driver.get('https://flipgrid.com/0d4b1f77')
    time.sleep(0.7)
    move if pyautogui.position() != (545, 932) else random.randint(1,2)
    pyautogui.click()
driver.close()
