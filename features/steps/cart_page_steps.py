from behave import when, then
from selenium.webdriver.common.by import By
from time import sleep

ADD_TO_CART = (By.XPATH, '//button[@data-test="chooseOptionsButton"]')
CONFIRM_TO_CART = (By.XPATH, '//button[@data-test="shippingButton"]')
CLOSE_DRAWER = (By.XPATH, '//button[@aria-label="close"]')
PRODUCT_NAME = (By.CSS_SELECTOR, '[data-test="cartItem-title"]')


@then('Verify empty cart message appears')
def verify_empty_cart_message(context):
    expected_cart_text = "Your cart is empty"
    actual_cart_text = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").text
    assert expected_cart_text == actual_cart_text, f"Error: Expected text {expected_cart_text} but got {actual_cart_text}"


@when('Click Add to cart on first product in search results')
def first_product_is_added(context):
    sleep(7)
    context.driver.find_element(*ADD_TO_CART).click()


@when('Click Add to cart from side navigation')
def confirm_is_added(context):
    sleep(3)
    context.driver.find_element(*CONFIRM_TO_CART).click()
    sleep(3)
    element = context.driver.find_element(*CLOSE_DRAWER)
    element.click()


@then('Verify {product_name} is added to cart')
def verify_product_name(context, product_name):
    actual_result = context.driver.find_element(*PRODUCT_NAME).text
    assert product_name in actual_result.lower(), f"Error: Expected {product_name} but got {actual_result}"
