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
 #print the title of the page
print(driver.title)  #print the title of the page


time.sleep(5)

ele = driver.find_element(By.ID,"email")

# print(ele.is_displayed())

# print(ele.is_enabled())


pass_ele = driver.find_element(By.ID,"pass")

# print(pass_ele.is_displayed())

# print(pass_ele.is_enabled())

ele.send_keys('reelsforyou')

pass_ele.send_keys('Squad1234')

driver.find_element(By.ID,'loginbutton').click()

time.sleep(666)