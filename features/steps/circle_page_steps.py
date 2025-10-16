from behave import given, when, then
from selenium.webdriver.common.by import By

from selenium.webdriver.support import wait

BENEFIT_CARDS = (By.CSS_SELECTOR, '[class="cell-item-content"]')


@given('Open Target Circle page')
def navigate_to_circle_page(context):
    context.driver.get('https://www.target.com/circle')



# @then('Verify at least {expected_amount} benefit cells display')
# def verify_10_benefit(context, expected_amount):
#     expected_amount = int(expected_amount)
#     cells = context.driver.find_elements(*BENEFIT_CARDS)
#     assert len(cells) >= expected_amount, f"Expected {expected_amount} benefit cells but got {len(cells)}"

