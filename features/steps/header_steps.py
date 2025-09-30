from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep

ACCOUNT_BUTTON = (By.ID, "account-sign-in")
SEARCH_FIELD = (By.ID, "search")
SEARCH_BUTTON = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
SIGNIN_BUTTON = (By.XPATH, "//*[@data-test='accountNav-signIn']")


@when('User clicks on Account button')
def click_account_button(context):
    context.driver.find_element(*ACCOUNT_BUTTON).click()
    sleep(2)


@when('User clicks on Sign In icon')
def click_sign_in(context):
    context.driver.find_element(*SIGNIN_BUTTON).click()
    sleep(3)


@when('Search for a {search_word}')
def search_product(context, search_word):
    context.driver.find_element(*SEARCH_FIELD).send_keys({search_word})
    context.driver.find_element(*SEARCH_BUTTON).click()
    sleep(5)


@when('User clicks on cart icon')
def click_cart_icon(context):
    context.driver.find_element(*CART_ICON).click()
    sleep(3)
