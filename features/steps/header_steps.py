from time import sleep

from behave import given, when, then
from selenium.webdriver.common.by import By

ACCOUNT_BUTTON = (By.ID, "account-sign-in")

SIGNIN_BUTTON = (By.XPATH, "//*[@data-test='accountNav-signIn']")


@when('User clicks on Account button')
def click_account_button(context):
    context.driver.find_element(*ACCOUNT_BUTTON).click()


@when('User clicks on Sign In icon')
def click_sign_in(context):
    context.driver.find_element(*SIGNIN_BUTTON).click()


@when('Search for {search_word}')
def search_product(context, search_word):
    context.app.header.search_product(search_word)


@when('Click on cart icon')
def click_cart_icon(context):
    context.app.header.click_cart_icon()
