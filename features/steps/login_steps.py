from behave import when, then, given


@then('Verify Sign In text is shown')
def verify_sign_in_text(context):
    context.app.signin_page.verify_sign_in_text()


@then('Verify Sign In button is shown')
def verify_sign_in_button(context):
    context.app.signin_page.verify_sign_in_button()


@when('User enters email {email}')
def enter_email(context, email):
    context.app.signin_page.enter_email(email)


@when('User selects to continue after email entry')
def select_continue_after_email_entry(context):
    context.app.signin_page.clicks_submit_button_after_email()


@when('User enters password {password}')
def enter_password(context, password):
    context.app.signin_page.enter_password(password)


@when('User selects to submit after password entry')
def select_continue_after_password_entry(context):
    context.app.signin_page.clicks_submit_button_after_password()


@then('Verify sign in is successful')
def verify_sign_in_is_successful(context):
    context.app.signin_page.sign_in_successful()


@then('Verify that incorrect password error message appears')
def verify_incorrect_password_error_message(context):
    context.app.signin_page.verify_warning_incorrectpw()
