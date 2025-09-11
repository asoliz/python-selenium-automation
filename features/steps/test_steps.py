from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep


@given('Open target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')
    sleep(3)


@when('Search for a product')
def search_product(context):
    context.driver.find_element(By.ID, "search").send_keys('chair')
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(5)


@then('Verify search results are shown')
def verify_search_results(context):
    actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='lp-resultsCount']").text
    expected_result = "chair"
    assert expected_result in actual_result, f"Error: Expected text {expected_result} but got {actual_result}"


@when('User clicks on cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()
    sleep(3)


@then('Verify empty cart message appears')
def verify_empty_cart_message(context):
    expected_cart_text = "Your cart is empty"
    actual_cart_text = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").text
    assert expected_cart_text == actual_cart_text, f"Error: Expected text {expected_cart_text} but got {actual_cart_text}"


@when('User clicks on Account button')
def click_account_button(context):
    context.driver.find_element(By.ID, "account-sign-in").click()
    sleep(2)


@when('User clicks on Sign In icon')
def click_sign_in(context):
    context.driver.find_element(By.XPATH, "//*[@data-test='accountNav-signIn']").click()
    sleep(2)


@then('Verify Sign In text is shown')
def verify_sign_in_text(context):
    expected_signin_text = "Sign in or create account"
    actual_signin_text = context.driver.find_element(By.XPATH, "//*[text()='Sign in or create account']").text
    assert expected_signin_text == actual_signin_text, f"Expected: {expected_signin_text} did not match Actual: {actual_signin_text}"


@then('Verify Sign In button is shown')
def verify_sign_in_button(context):
    context.driver.find_element(By.XPATH, "//button[normalize-space()='Sign in with passkey']")
