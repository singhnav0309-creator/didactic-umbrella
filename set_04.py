from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()

driver.get("https://www.google.com")
time.sleep(20)
driver.maximize_window()
time.sleep(20)
driver.maximize_window()

search_box = driver.find_element(By.NAME,"q")
search_box.send_keys("selenium")
search_box.send_keys(Keys.ENTER)
time.sleep(20)

driver.back()
time.sleep(20)

driver.forward()
time.sleep(20)

driver.quit()