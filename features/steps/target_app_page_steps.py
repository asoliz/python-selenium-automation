from time import sleep

from behave import given, when, then


@given('Open Target App page')
def open_target_app_page(context):
    context.app.target_app_page.open_target_app()


@when('Click Privacy Policy Link')
def click_privacy_link(context):
    context.app.target_app_page.click_privacy_link()


@then('Verify Privacy Policy page opened')
def verify_pp_opened(context):
    context.app.privacy_policy_page.verify_pp_opened()


@given('Store original window')
def store_window(context):
    context.original_window = context.app.page.get_original_window()
    print('Original window: ', context.original_window)


@when('Switch to new window')
def switch_window(context):
    context.app.page.switch_to_newly_opened_window([context.original_window])


@then('Close current page')
def close_page(context):
    context.app.page.close()


@then('Return to original window')
def switch_to_original_window(context):
    context.app.page.switch_to_window_by_id(context.original_window)
    sleep(2)
