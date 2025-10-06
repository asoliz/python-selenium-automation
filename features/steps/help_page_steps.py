from behave import given, when, then
from selenium.webdriver.common.by import By

HELP_TITLE = (By.XPATH, "//h1[text()='Help']")
HAVE_A_QUESTION_TEXT = (By.XPATH, "//h1[text()='Have a question?']")


@given('Open target help page')
def open_main(context):
    context.driver.get('https://help.target.com/help')


# @then('Verify these UI elements are present of the page')
# def verify_page_elements(context):
#     assert len(cells) >= expected_amount, f"Expected {expected_amount} benefit cells but got {len(cells)}"
