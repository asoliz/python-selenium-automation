from behave import given, when, then
from selenium.webdriver.common.by import By


@given('Open target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')


