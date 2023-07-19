from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


# creating driver object
driver = webdriver.Chrome()
#specifying the web page we want to access
driver.get("https://www.google.com/")
 #print the title of the page
print(driver.title)
#find a button using find method and click the button
driver.find_element(By.CLASS_NAME, "gb_v").click()
#sleep for 5 sec
time.sleep(5)
#close the current page
driver.close()