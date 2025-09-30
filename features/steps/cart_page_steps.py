from behave import when, then
from selenium.webdriver.common.by import By
from time import sleep

ADD_TO_CART = (By.CSS_SELECTOR, '[id*="addToCartButton"]')
CONFIRM_TO_CART = (By.CSS_SELECTOR, '[data-test="content-wrapper"] [id*="addToCartButtonOrTextId"]')
CLOSE_DRAWER = (By.CSS_SELECTOR, '[aria-label="close"]')
PRODUCT_NAME = (By.CSS_SELECTOR, '[data-test="cartItem-title"]')


@then('Verify empty cart message appears')
def verify_empty_cart_message(context):
    expected_cart_text = "Your cart is empty"
    actual_cart_text = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").text
    assert expected_cart_text == actual_cart_text, f"Error: Expected text {expected_cart_text} but got {actual_cart_text}"


@when('First product in search results is added to cart')
def first_product_is_added(context):
    context.driver.find_element(*ADD_TO_CART).click()
    sleep(3)


@when('Confirm product is added to cart')
def confirm_is_added(context):
    context.driver.find_element(*CONFIRM_TO_CART).click()
    sleep(5)
    context.driver.find_element(*CLOSE_DRAWER).click()


@then('Verify {product_name} is added to cart')
def verify_product_name(context, product_name):
    actual_result = context.driver.find_element(*PRODUCT_NAME).text
    assert actual_result in product_name, f"Error: Expected {product_name} but got {actual_result}"
