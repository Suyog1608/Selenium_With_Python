import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("file:///D:/Selenium_With_Python/Python-Selenium/html_code.html")
login_form = driver.find_element(by=By.ID, value='loginForm')
print("My login form element is:")
print(login_form)
time.sleep(8)
driver.close()
