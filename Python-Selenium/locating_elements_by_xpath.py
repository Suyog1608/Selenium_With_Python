from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("file:///D:/Selenium_With_Python/Python-Selenium/html_code.html")
login_form_absolute = driver.find_element(by=By.XPATH, value="/html/body/form[1]")
login_form_relative = driver.find_element(by=By.XPATH, value="//form[1]")
login_form_id = driver.find_element(by=By.XPATH, value="//form[@id='loginForm']")
print("My login form is: ")
print(login_form_absolute)
print(login_form_relative)
print(login_form_id)
time.sleep(8)
driver.close()