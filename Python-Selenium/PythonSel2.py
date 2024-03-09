from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://github.com/Suyog1608")

time.sleep(8)
driver.close()