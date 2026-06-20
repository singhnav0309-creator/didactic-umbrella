from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()

driver.get('https://www.amazon.in')

driver.maximize_window()
time.sleep(8)

driver.find_element(By.ID,"twotabsearchtextbox").send_keys("Laptop Tables")
driver.find_element(By.ID, "nav-search-submit-button").click()

products = driver.find_elements(By.CSS_SELECTOR,"a-size-medium a-spacing-none a-color-base a-text-normal")

print(len(products))

for product in products:
    product.click()

print(driver.title)

driver.quit()


