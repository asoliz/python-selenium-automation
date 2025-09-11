from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# 1. Find the most optimal locators for StackOverflow
# Create Account page elements
driver.get('https://stackoverflow.com/users/signup')
sleep(3)
# Create your account
text = driver.find_element(By.CSS_SELECTOR, ".fs-headline1.fw-bold").text
print(text)
# TOC link
driver.find_element(By.CSS_SELECTOR, "[name=tos]")
# Privacy Policy link
driver.find_element(By.CSS_SELECTOR, "[name=privacy]")
# email input field
driver.find_element(By.CSS_SELECTOR, "#email")
# password input field
driver.find_element(By.CSS_SELECTOR, "#password")
# reveal password button
driver.find_element(By.CSS_SELECTOR, ".ps-absolute.js-show-password")
# Sign Up button
driver.find_element(By.CSS_SELECTOR, "#submit-button")
# Sign Up with Google button
driver.find_element(By.CSS_SELECTOR, "button.s-btn__google")
# Sign Up with GitHub button
driver.find_element(By.CSS_SELECTOR, "button.s-btn__github")
# Link for teams upt to 50
driver.find_element(By.CSS_SELECTOR, "[href='https://stackoverflow.com/teams?utm_source=so-owned&utm_medium=product&utm_campaign=free-50&utm_content=public-sign-up']")

# 2. Create a test case using BDD that opens target.com, clicks on the cart icon and verifies that “Your cart is empty” message is shown:
# Open target.com
# Click on Cart icon
# Verify “Your cart is empty” message is shown
#
# 3. Create a test case using BDD to verify that a logged out user can navigate to Sign In:
# Open target.com
# Click Sign In
# From right side navigation menu, click Sign In
# Verify Sign In form opened
#
# Assessment Criteria
# The locators accurately identify the intended page elements and demonstrate efficiency in terms of performance and maintainability.
# The test cases follow the principles of BDD and work correctly
