from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/")

find_id = driver.find_element(by=By.ID, value="td-block-0")
print("the id element is:")
print(find_id)

find_class_name = driver.find_element(by=By.CLASS_NAME, value="no-js")
print("the class element is: ")
print(find_class_name)

find_head = driver.find_element(by=By.XPATH, value="//meta[1]")
print("the Xpath element is: ")
print(find_head)

find_name = driver.find_element(by=By.NAME, value="generator")
print("the name element is: ")
print(find_name)

time.sleep(5)
driver.close()
