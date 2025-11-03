from behave import when, then, given


@then('Verify Sign In text is shown')
def verify_sign_in_text(context):
    context.app.signin_page.verify_sign_in_text()


@then('Verify Sign In button is shown')
def verify_sign_in_button(context):
    context.app.signin_page.verify_sign_in_button()


@when('User enters email {email}')
def enter_email(context, email):
    context.app.signin_page.enter_email_then_submit(email)


@when('User enters password {password}')
def enter_password(context, password):
    context.app.signin_page.enter_password_then_submit(password)


@then('Verify sign in is successful')
def verify_sign_in_is_successful(context):
    context.app.signin_page.sign_in_successful()
