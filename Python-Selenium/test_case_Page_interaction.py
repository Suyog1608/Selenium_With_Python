from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.python.org/")

search = driver.find_element(by=By.NAME, value="q")
search.clear()
search.send_keys("pycon")
search.send_keys(Keys.RETURN)
time.sleep(5)

driver.close()