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

# [Optional] Build a test case yourself from scratch to search for a product on Target (same as shown in the class), make sure it works and you remember selenium commands.
# 1. Open https://www.target.com/
driver.get('https://www.target.com/')
sleep(3)

# 2. Search for a product - "chair"
driver.find_element(By.ID, "search").send_keys('chair')
driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
sleep(5)

# 3. Verify text
actual_result = driver.find_element(By.XPATH, "//div[@data-test='lp-resultsCount']").text
expected_result = "chair"
assert expected_result in actual_result, f"Error: Expected text {expected_result} but got {actual_result}"

driver.quit()
