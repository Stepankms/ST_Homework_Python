from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)

driver.get("https://the-internet.herokuapp.com/login")

user = driver.find_element(By.CSS_SELECTOR, "input#username")
user.send_keys("tomsmith")
password = driver.find_element(By.CSS_SELECTOR, "input#password")
password.send_keys("SuperSecretPassword!")

button = driver.find_element(By.CSS_SELECTOR, "button.radius")
button.click()

flash = driver.find_element(By.CSS_SELECTOR, "div#flash")
print(flash.text)

driver.quit()
