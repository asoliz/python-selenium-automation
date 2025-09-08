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

# 1. Practice with locators.
# Create locators + search strategy for these page elements of Amazon Sign in page:
driver.get('https://www.amazon.com')
sleep(3)
driver.find_element(By.ID, "nav-link-accountList").click()
sleep(3)

# Amazon logo, search by Class, "a-link-nav-icon"
driver.find_element(By.CLASS_NAME, "a-link-nav-icon")
# Email field, search by ID, "ap_email"
driver.find_element(By.ID, "ap_email")
# Continue button, search by ID, "continue"
driver.find_element(By.ID, "continue")
# Conditions of use link, search by ID and LinkText
driver.find_element(By.XPATH, "//*[@id='legalTextRow']//a[text()='Conditions of Use']")
# Privacy Notice link
driver.find_element(By.XPATH, "//*[@id='legalTextRow']//a[text()='Privacy Notice']")
# Need help link, search by Class, "a-expander-prompt"
driver.find_element(By.CLASS_NAME, "a-expander-prompt")
# Forgot your password link , search by ID, "auth-fpp-link-bottom"
driver.find_element(By.ID, "auth-fpp-link-bottom")
# Other issues with Sign-In link, search by ID, "ap-other-signin-issues-link"
driver.find_element(By.ID, "ap-other-signin-issues-link")
# Create your Amazon account button, search by ID, "createAccountSubmit"
driver.find_element(By.ID, "createAccountSubmit")

driver.quit()
