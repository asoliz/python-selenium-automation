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
driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')
sleep(3)

# Amazon logo, search by Class, "a-link-nav-icon"
driver.find_element(By.CLASS_NAME, "a-link-nav-icon")
# Email field, search by ID, "ap_email"
driver.find_element(By.ID, "ap_email")
# Continue button, search by ID, "continue"
driver.find_element(By.ID, "continue")
# Conditions of use link, search by ID and LinkText
driver.find_element(By.XPATH, "//div[@id='legalTextRow']//a[contains(@href, 'ap_signin_notification_condition_of_use')]")
# Privacy Notice link
driver.find_element(By.XPATH, "//div[@id='legalTextRow']//a[contains(@href, 'ap_signin_notification_privacy_notice')]")
# Need help link, search by Class, "a-expander-prompt"
driver.find_element(By.CLASS_NAME, "a-expander-prompt")
# Forgot your password link , search by ID, "auth-fpp-link-bottom"
driver.find_element(By.ID, "auth-fpp-link-bottom")
# Other issues with Sign-In link, search by ID, "ap-other-signin-issues-link"
driver.find_element(By.ID, "ap-other-signin-issues-link")
# Create your Amazon account button, search by ID, "createAccountSubmit"
driver.find_element(By.ID, "createAccountSubmit")

driver.quit()
