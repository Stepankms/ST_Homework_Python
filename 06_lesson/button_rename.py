from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
waiter = WebDriverWait(driver, 40, 0.1)

driver.get("https://uitestingplayground.com/textinput")

input = driver.find_element(By.CSS_SELECTOR, "#MyButton")

input.send_keys("SkyPro")

waiter.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#MyButton"), "SkyPro")
)

driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()

txt = print(driver.find_element(By.CSS_SELECTOR, "#updatingButton").text)
print(txt)

driver.quit()
