from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
 
 
print(driver.title)

driver.find_element(By.CLASS_NAME, "gb_v").click()

time.sleep(5)

driver.close()