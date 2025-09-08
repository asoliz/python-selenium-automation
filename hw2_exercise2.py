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

# 2. Create a test case for the SignIn page using python & selenium script.
# (Make sure to use Incognito browser mode when searching for locators)

# Test Case: Users can navigate to SignIn page
# 1. Open https://www.target.com/
driver.get('https://www.target.com/')
sleep(3)

# 2. Click Account button
driver.find_element(By.ID, "account-sign-in").click()
sleep(2)

# 3. Click SignIn btn from side navigation
driver.find_element(By.XPATH, "//*[@data-test='accountNav-signIn']").click()
sleep(3)

# 4. Verify SignIn page opened:
# “Sign in or create account” text is shown,
driver.find_element(By.XPATH, "//*[text()='Sign in or create account']")
# SignIn button is shown (you can just use driver.find_element() to check for element’s presence, no need to assert here)
driver.find_element(By.XPATH, "//button[normalize-space()='Sign in with passkey']").click()
