from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()

driver.get("https://www.amazon.in")
driver.maximize_window()

time.sleep(30)

select = driver.find_element(By.LINK_TEXT,"Mobiles")
select.click()

select_01 = driver.find_element(By.LINK_TEXT,"Cameras")
select_01.click()

driver.refresh()

