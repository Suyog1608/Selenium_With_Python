from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.python.org/")

find_id = driver.find_element(by=By.ID, value="submit")
print("the element id is: ")
print(find_id)

find_name = driver.find_element(by=By.NAME, value="submit")
print("the element name is: ")
print(find_name)

find_xpath = driver.find_element(by=By.XPATH, value="//header/div/h1/a/img")
print("the xpath element is: ")
print(find_xpath)

find_class_name = driver.find_element(by=By.CLASS_NAME, value="search-button")
print("the class element is: ")
print(find_class_name)

time.sleep(5)
driver.close()