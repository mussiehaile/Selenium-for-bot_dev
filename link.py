from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


# seting up incognito mode and instanciating driver
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
driver = webdriver.Chrome(options=options)

#open the given url using driver
driver.get('https://www.facebook.com/login/')
#find all the liks using tag name
lin=  driver.find_elements(By.TAG_NAME,"a")
#counting number of links
print(len(lin))

driver.find_element(By.LINK_TEXT,"Forgot account?").click()
