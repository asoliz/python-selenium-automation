from behave import given, when, then
from selenium.webdriver.common.by import By

SEARCH_RESULTS_TXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")

@then('Verify search results are shown for {product}')
def verify_search_results(context, product):
    actual_result = context.driver.find_element(*SEARCH_RESULTS_TXT).text
    assert product in actual_result, f"Error: Expected text {product} but got {actual_result}"
