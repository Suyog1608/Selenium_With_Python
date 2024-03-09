from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.get('https://chromedriver.chromium.org/getting-started')
time.sleep(10)