from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("https://wiki.python.org/moin/Frontpage")

search_box = driver.find_element(by=By.ID, value="searchinput")
search_box.clear()
search_box.send_keys("Beginner")
search_box.send_keys(Keys.RETURN)
time.sleep(5)

more_actions = Select(driver.find_element(by=By.XPATH, value="//*[@id='sidebar']/div[3]/ul/li[5]/form/div/select"))
more_actions.select_by_visible_text("Raw Text")
time.sleep(5)

driver.close()