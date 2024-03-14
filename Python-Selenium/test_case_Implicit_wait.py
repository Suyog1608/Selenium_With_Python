from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.implicitly_wait(10)

driver.get("https://www.python.org")
myDynamicElement = driver.find_element(by=By.ID, value="start-shell")

driver.close()
