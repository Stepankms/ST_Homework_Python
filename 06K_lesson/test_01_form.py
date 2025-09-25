import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

 
def test_buttons():
    options = webdriver.EdgeOptions()
    driver = webdriver.Edge(options=options)
    
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.implicitly_wait(4)
 
    # Заполняем обязательные поля
    first_name = driver.find_element(By.CSS_SELECTOR, '[name="first-name"]')
    first_name.send_keys('Иван')
 
    last_name = driver.find_element(By.CSS_SELECTOR, '[name="last-name"]')
    last_name.send_keys('Петров')
 
    address = driver.find_element(By.CSS_SELECTOR, '[name="address"]')
    address.send_keys('Ленина, 55-3')
 
    email = driver.find_element(By.CSS_SELECTOR, '[name="e-mail"]')
    email.send_keys('test@skypro.com')
 
    phone_number = driver.find_element(By.CSS_SELECTOR, '[name="phone"]')
    phone_number.send_keys('+7985899998787')
 
    city = driver.find_element(By.CSS_SELECTOR, '[name="city"]')
    city.send_keys('Москва')
 
    # Заполняем дополнительные поля
    country = driver.find_element(By.CSS_SELECTOR, '[name="country"]')
    country.send_keys('Россия')
    
    job_position = driver.find_element(By.CSS_SELECTOR, '[name="job-position"]')
    job_position.send_keys('QA')
    
    company = driver.find_element(By.CSS_SELECTOR, '[name="company"]')
    company.send_keys('SkyPro')
 
    submit_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".btn.btn-outline-primary.mt-3"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    driver.execute_script("arguments[0].click();", submit_button)
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "main[class=flex-shrink-2]"))
    )
    
    zip_code_field = driver.find_element(By.CSS_SELECTOR, "div#zip-code")
    assert "alert-danger" in zip_code_field.get_attribute("class")

    green_highlighted_fields = driver.find_elements(
        By.CSS_SELECTOR, "div.alert.py-2.alert-success")
    assert len(green_highlighted_fields) == 9
    
