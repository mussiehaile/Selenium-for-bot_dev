from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


options = webdriver.ChromeOptions()
options.add_argument("--incognito")

driver = webdriver.Chrome(options=options)
# creating driver object
# driver = webdriver.Chrome()
#specifying the web page we want to access
driver.get('https://www.facebook.com/login/')


driver.implicitly_wait(14)  # implicit wait  is saying webridver to wait 10 seco befor the exception is raied.
assert "Log into Facebook" in driver.title
 #print the title of the page
# print(driver.title)  #print the title of the page


ele = driver.find_element(By.ID,"email")
pass_ele = driver.find_element(By.ID,"pass")

ele.send_keys('reelsforyou')
pass_ele.send_keys('Squad1234')
driver.find_element(By.ID,'loginbutton').click()