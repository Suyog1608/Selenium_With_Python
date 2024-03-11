from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("file:///D:/Selenium_With_Python/Python-Selenium/html_code.html")

content = driver.find_element(by=By.CLASS_NAME, value="content")
print("My content element is: ")
print(content)

time.sleep(8)
driver.close()