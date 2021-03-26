import selenium
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://flipgrid.com/0d4b1f77')

joinMS = driver.find_element_by_link_text('Join with Microsoft')
joinMS.click()
