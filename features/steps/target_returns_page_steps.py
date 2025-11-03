from behave import given, when, then

@given('Open target returns page')
def open_help_returns_page(context):
    context.app.target_returns_page.open_help_returns_page()

@then('Verify Help Returns page opened')
def verify_returns_page(context):
    context.app.target_returns_page.verify_returns_header()

@when('Select {help_topic} in Help dropdown menu')
def select_help_topic(context, help_topic):
    context.app.target_returns_page.select_helptopics_dropdown(help_topic)

@then('Verify {help_topic_page} age opens')
def verify_helptopic_header(context, help_topic_page):
    context.app.target_returns_page.verify_header_help_topic(help_topic_page)
