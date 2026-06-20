### SELENIUM AUTOMATION PROJECT

## OVERVIEW
# This project describes about Automation of web browser using Selenium Webdriver in Python.
  This automation helps in opening websites, locating web elements, entering text, navigating between pages, etc.

## TECHNOLOGIES USED
# Python 3.x
# Selenium Webdriver
# Microsoft Edge Browser
# Visual Studio Code
# Selenium
## PROJECT FEATURES
# Automatically launch web browser
# open amazon website
# Enter search keywords
# Submit search Query
# Alternatively, open Google search
# Enter search keywords
# Submit search Query
# Navigate backward and forward
# Automatically close web browser

## HOW TO RUN?
# Download and Install Python

# pip install selenium

# install Microsoft Edge Browser

# Clone the repository
  git clone https://github.com/singhnav0309-creator/didactic-umbrella

# Navigate to project folder
  cd selenium-automation-project

# Run script
  python main.py

## PROJECT STRUCTURE
# selenium-automation-project
  |-README.md
  |-set_01.py
  |-set_02.py
  |-set_03.py
  |-set_04.py
  |-main.py

## FOR EXAMPLE (Code)
# from selenium import webdriver
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

## AUTHOR
# Navjot Singh
