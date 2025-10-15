from behave import when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

ADD_TO_CART = (By.XPATH, '//button[@data-test="chooseOptionsButton"]')
CONFIRM_TO_CART = (By.XPATH, '//button[@data-test="shippingButton"]')
CLOSE_DRAWER = (By.CSS_SELECTOR, '[aria-label="close"]')
PRODUCT_NAME = (By.CSS_SELECTOR, '[data-test="cartItem-title"]')

SEARCH_RESULTS = (By.XPATH, '//div[@data-test="lp-resultsCount"]')


@then('Verify empty cart message appears')
def verify_empty_cart_message(context):
    context.app.cart_page.verify_empty_cart_message()

@when('Click Add to cart on first product in search results')
def first_product_is_added(context):
    context.driver.wait.until(
        EC.presence_of_element_located(SEARCH_RESULTS),
        message="Search results did not load")
    context.driver.find_element(*ADD_TO_CART).click()


@when('Click Add to cart from side navigation')
def confirm_is_added(context):
    context.driver.find_element(*CONFIRM_TO_CART).click()
    context.driver.find_element(*CLOSE_DRAWER).click()


@then('Verify {product_name} is added to cart')
def verify_product_name(context, product_name):
    actual_result = context.driver.find_element(*PRODUCT_NAME).text
    assert product_name in actual_result.lower(), f"Error: Expected {product_name} but got {actual_result}"
