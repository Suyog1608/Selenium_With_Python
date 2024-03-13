from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("file:///D:/Selenium_With_Python/Python-Selenium/html_code1.html")

select = Select(driver.find_element(by=By.NAME, value="numReturnSelect"))
select.select_by_index(4)
time.sleep(5)

select.select_by_visible_text("200")
time.sleep(5)

select.select_by_value("250")
time.sleep(5)

options = select.options
print(options)

submit_button = driver.find_element(by=By.NAME, value="continue")
submit_button.submit()
time.sleep(5)

driver.close()