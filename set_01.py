from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()

driver.get("https://www.google.com")

input = driver.find_element(By.NAME, "q")
input.send_keys("selenium")
time.sleep(500)





