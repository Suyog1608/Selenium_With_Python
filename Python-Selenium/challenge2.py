from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/")

find_id = driver.find_element(by=By.ID, value="navbarDropdown")
print("The element id is :")
print(find_id)

find_name = driver.find_element(by=By.NAME, value="submit")
print("the name element is: ")
print(find_name)

find_Xpath = driver.find_element(by=By.XPATH, value="//section[1]/div/div/div/h1")
print("The Xpath element is: ")
print(find_Xpath)

find_class_name = driver.find_element(by=By.CLASS_NAME, value="row")
print("the class element is: ")
print(find_class_name)

time.sleep(5)
driver.close()