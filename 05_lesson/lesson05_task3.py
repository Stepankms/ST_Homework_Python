from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)

driver.get("http://the-internet.herokuapp.com/inputs")

input = driver.find_element(By.CSS_SELECTOR, "input")

input.send_keys("Sky")

sleep(5)

input.clear()

sleep(5)

input.send_keys("Pro")

sleep(5)

driver.quit()
