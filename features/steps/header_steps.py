from behave import when, then
from selenium.webdriver.common.by import By

HEADER_LINKS = (By.XPATH, '//a[contains(@data-test, "@web/GlobalHeader/UtilityHeader/")]')
TARGET_CIRCLE_HEADER = (By.XPATH, '//div[@data-test="@web/Circle/PageTitle"]')


@when('User clicks on Account button')
def click_account_button(context):
    context.app.header.click_account_button()


@when('User clicks on Sign In icon')
def click_sign_in(context):
    context.app.side_navigation.click_signin_button()


@when('Search for {search_word}')
def search_product(context, search_word):
    context.app.header.search_product(search_word)


@when('Click on cart icon')
def click_cart_icon(context):
    context.app.header.click_cart_icon()


@when('Click on 1st header link')
def click_1st_link(context):
    element = context.driver.find_element(*HEADER_LINKS)
    context.driver.refresh()
    element.click()


@then('Verify header has {expected_amount} links')
def verify_header_link_counts(context, expected_amount):
    expected_amount = int(expected_amount)
    links = context.driver.find_elements(*HEADER_LINKS)
    print(f'Links {links}')
    assert len(links) == expected_amount, f'Expected {expected_amount} links, but got {len(links)}'


@then('Verify Target Circle opens')
def verify_header_link_count(context):
    context.driver.find_element(*TARGET_CIRCLE_HEADER)
