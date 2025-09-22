import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

 
options = webdriver.EdgeOptions()
driver = webdriver.Edge(options=options)
        
driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

input = driver.find_element(By.CSS_SELECTOR, '#delay')
input.send_keys('1')

button_7 = driver.find_element(By.XPATH, '//span[text()="7"]').click()
button_plus = driver.find_element(By.XPATH, '//span[text()="+"]').click()
button_8 = driver.find_element(By.XPATH, '//span[text()="8"]').click()
button_equals = driver.find_element(By.XPATH, '//span[text()="="]').click()
waiter = WebDriverWait(driver, 52)
waiter.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div.screen'), '15'))

result = driver.find_element(By.CSS_SELECTOR, 'div.screen').text
print(result)

assert result == '15'

driver.quit