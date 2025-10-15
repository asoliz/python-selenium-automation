from behave import given, when, then
from selenium.webdriver.common.by import By


@given('Open target main page')
def open_main(context):
    context.app.main_page.open_main()


