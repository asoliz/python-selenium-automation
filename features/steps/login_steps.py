from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep


@then('Verify Sign In text is shown')
def verify_sign_in_text(context):
    expected_signin_text = "Sign in or create account"
    actual_signin_text = context.driver.find_element(By.XPATH, "//*[text()='Sign in or create account']").text
    assert expected_signin_text == actual_signin_text, f"Expected: {expected_signin_text} did not match Actual: {actual_signin_text}"


@then('Verify Sign In button is shown')
def verify_sign_in_button(context):
    context.driver.find_element(By.XPATH, "//button[normalize-space()='Sign in with passkey']")
