from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep

BENEFIT_CARDS = (By.CSS_SELECTOR, '[class="cell-item-content"]')


@given('Open Target Circle page')
def open_main(context):
    context.driver.get('https://www.target.com/circle')
    sleep(3)


@then('Verify at least {expected_amount} benefit cells display')
def verify_10_benefit(context, expected_amount):
    expected_amount = int(expected_amount)
    cells = context.driver.find_elements(*BENEFIT_CARDS)
    assert len(cells) >= expected_amount, f"Expected {expected_amount} benefit cells but got {len(cells)}"

