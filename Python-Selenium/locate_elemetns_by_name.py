from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("file:///D:/Selenium_With_Python/Python-Selenium/html_code.html")
username = driver.find_element(by=By.NAME, value='username')
print("My element name is:")
print(username)
time.sleep(8)
driver.close()
