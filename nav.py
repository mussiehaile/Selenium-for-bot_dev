from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time



# creating driver object
driver = webdriver.Chrome()
#specifying the web page we want to access
driver.get("https://www.google.com/")
 #print the title of the page
print(driver.title)  #print the title of the page


## we will perform page navigation using back and forward method


#specify the second page url
driver.get('https://selenium-python.readthedocs.io/index.html')
print(driver.title)   #print the title of the page

# back to the previous page
driver.back()
time.sleep(4)    #sleep for the 4 sec
print(driver.title)


#now forward to the previous page
driver.forward()
time.sleep(4)   #sleep for the 4 sec
print(driver.title)